# 공공데이터포털 한국환경공단_전기자동차 충전소 정보 api 를 이용한 웹크롤링
# https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15076352
# 참조 웹페이지: 웹 크롤링 - [Python] 전기차 충전소 이용률 구하기 - https://haries.tistory.com/19
# v0.3 시간간격을 1분으로 변경
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import time
import schedule
import datetime


url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerInfo?'
# 본인 서비스키를 입력하세요!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ServiceKey = 'WQ3OLgIT9KBQOZ1kOrn1hS5akC%2BuhQzyXiisG75us6v0XxTW03gCZNINODnPBpMrfuLNH2BG4bOG8B9QOo8A8g%3D%3D'

# 지역코드 입력하세요
z = 48
###################################

# 지역코드 확인: https://www.code.go.kr/stdcode/regCodeL.do 에서 광역자치단체 번호 앞 두자리 활용

names = []  # 이름
charge_types = []  # 충전기 타입
addresss = []  # 주소
latitudes = []  # 위도
longitudes = []  # 경도
states = []  # 충전기 상태
outputs = []  # 충전용량 3, 7, 50, 100, 200
methods = []  # 충전방식 단독 or 동시
zcodes = []  # 지역코드
limityns = []  # 이용자 제한 Y or N
limitdetails = []  # 이용자 제한 사유
parking_frees = []   # 주차료 무료 Y or N


page_num = 1
while 1:
    response = (url + 'ServiceKey=' + ServiceKey + '&numOfRows=1000' +
                '&pageNo=' + str(page_num) + '&zcode=' + str(z))
    url_new = response.encode('utf-8')
    req = requests.get(url_new)
    bs = BeautifulSoup(req.text, 'html.parser')

    name = bs.findAll('statnm')
    charge_type = bs.findAll('chgertype')
    address = bs.findAll('addr')
    latitude = bs.findAll('lat')
    longitude = bs.findAll('lng')
    state = bs.findAll('stat')
    output = bs.findAll('output')
    method = bs.findAll('method')
    zcode = bs.findAll('zcode')
    limityn = bs.findAll('limitYn')
    limitdetail = bs.findAll('limitDetail')
    parking_free = bs.findAll('parkingfree')

    total_num = str(bs.find('totalcount'))
    total = int(re.findall('\d+', total_num)[0])

    if page_num < total // 1000 + 1:
        for i in range(1000):
            names.append(name[i].text)
            charge_types.append(charge_type[i].text)
            addresss.append(address[i].text)
            latitudes.append(latitude[i].text)
            longitudes.append(longitude[i].text)
            states.append(state[i].text)
            outputs.append(output[i].text)
            methods.append(method[i].text)
            zcodes.append(zcode[i].text)
            try:
                limityns.append(limityn[i].text)
                limitdetails.append(limitdetail[i].text)
            except:
                limityns.append('')
                limitdetails.append('')
            parking_frees.append(parking_free[i].text)

        page_num += 1

    else:
        for i in range(total % 1000):
            names.append(name[i].text)
            charge_types.append(charge_type[i].text)
            addresss.append(address[i].text)
            latitudes.append(latitude[i].text)
            longitudes.append(longitude[i].text)
            states.append(state[i].text)
            outputs.append(output[i].text)
            methods.append(method[i].text)
            zcodes.append(zcode[i].text)
            try:
                limityns.append(limityn[i].text)
                limitdetails.append(limitdetail[i].text)
            except:
                limityns.append('')
                limitdetails.append('')
            parking_frees.append(parking_free[i].text)

        break

# 시간마다 충전소 상태를 가져오게 만드는 함수


def store_one_hour_state():
    states = []
    page_num = 1
    while 1:
        response = (url + 'ServiceKey=' + ServiceKey + '&numOfRows=1000' +
                    '&pageNo=' + str(page_num) + '&zcode=' + str(z))  # zcode 50이 제주도
        url_new = response.encode('utf-8')
        req = requests.get(url_new)
        bs = BeautifulSoup(req.text, 'html.parser')

        state = bs.findAll('stat')

        total_num = str(bs.find('totalcount'))
        total = int(re.findall('\d+', total_num)[0])

        if page_num >= total // 1000 + 1:
            for i in range(total % 1000):
                states.append(state[i].text)
            break

        else:
            for i in range(1000):
                states.append(state[i].text)
            page_num += 1
    states
    return states


# 초기 데이터를 잘 받아왔는지 확인해보는 코드입니다. 보니까 이용자제한, 이용제제한사유 같은 칼럼은 데이터가 하나도 없네요. 애초에 왜 환경공단 사람들이 만들어놨는지 모르겠어요
first_lists_data = pd.DataFrame([names, charge_types, addresss, latitudes, longitudes,
                                outputs, methods, zcodes, limityns, limitdetails, parking_frees, states]).T
first_lists_data.columns = ['이름', '충전타입', '주소', '위도', '경도', '출력',
                            '충전방식', '지역코드', '이용자제한', '이용자제한사유', '무료 주차', '실시간 상태(5분)']
# print(first_lists_data)


# 10초마다


# 0시간부터 1시간까지의 데이터 저장
cumulative_data0_1 = first_lists_data
for i in range(1, 2):  # 1시간 돌리려면 (1,20)
    # 1200초 = 20분, for문 안에 코딩 실행하는데 5초 걸림. 1195초 마다 실행시키면 1195초마다 for문 실행 됨
    time.sleep(55)
    now_state_data = store_one_hour_state()
    minutes = (i*1) % 60
    hours = (i*1)//60
    now = str(hours) + ' : ' + str(minutes)
    now_state_data = pd.DataFrame(now_state_data, columns=[now])
    cumulative_data0_1 = pd.concat(
        [cumulative_data0_1, now_state_data], axis=1)
    # cumulative_data0_1

final_data = cumulative_data0_1  # 여태껏 모은 데이터 저장
# final_data.head()

final_data.to_csv("./Public_Data/한국환경공단/output/Ev_charging_48.csv",
                  mode='w', encoding='utf-8-sig')
