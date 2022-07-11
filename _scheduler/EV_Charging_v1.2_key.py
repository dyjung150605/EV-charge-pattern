# 공공데이터포털 한국환경공단_전기자동차 충전소 정보 api 를 이용한 웹크롤링
# https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15076352
# 참조 웹페이지: 웹 크롤링 - [Python] 전기차 충전소 이용률 구하기 - https://haries.tistory.com/19
# v0.4 가져올 필드 수정
from fileinput import filename
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from datetime import datetime
import os

url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerInfo?'
# 본인 서비스키를 입력하세요!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ServiceKey = 'Vo%2Fw4guZqRxhnMdOxKYcoGkhLB5YitCGlieIui0XAvtWB64mpG6xLZ%2Fc4JGi65dmkneDGxjyiSsmaAp4%2BknZsw%3D%3D'

names = []  # 충전소명

stat_ids = []  # 충전소ID *추가
chger_ids = []  # 충전기ID *추가

charge_types = []  # 충전기 타입
addresss = []  # 주소
latitudes = []  # 위도
longitudes = []  # 경도
states = []  # 충전기 상태

stat_upddts = []  # 상태갱신일시 *추가
lasttsdts = []  # 마지막 충전시작일시 *추가
lasttedts = []  # 마지막 충전종료일시 *추가
nowtsdts = []  # 충전중 시작일시 *추가

outputs = []  # 충전용량 3, 7, 50, 100, 200
methods = []  # 충전방식 단독 or 동시
zcodes = []  # 지역코드
limityns = []  # 이용자 제한 Y or N
limitdetails = []  # 이용자 제한 사유
parking_frees = []   # 주차료 무료 Y or N

usetimes = []  # 충전기 이용가능시간
busiids = []  # 기관아이디
bnms = []  # 기관명
businms = []  # 운영기관명
delyns = []  # 삭제 여부
deldetails = []  # 삭제 사유
notes = []  # 충전소 안내

now = datetime.now()
nowtext = now.strftime('%Y%m%d%H%M%S')

# 지역코드 입력하세요
# 지역코드 확인: https://www.code.go.kr/stdcode/regCodeL.do 에서 광역자치단체 번호 앞 두자리 활용
# 11: 서울특별시
# 26: 부산광역시
# 27: 대구광역시
# 28: 인천광역시
# 29: 광주광역시
# 30: 대전광역시
# 31: 울산광역시
# 36: 세종특별자치시
# 41: 경기도
# 42: 강원도
# 43: 충청북도
# 44: 충청남도
# 45: 전라북도
# 46: 전라남도
# 47: 경상북도
# 48: 경상남도
# 50: 제주특별자치도
# code_region = [11, 26, 27, 28, 29, 30, 31,
#                36, 41, 42, 43, 44, 45, 46, 47, 48, 50]

# for z in code_region:
page_num = 1
while 1:
    # response = (url + 'ServiceKey=' + ServiceKey + '&numOfRows=1000' +
    #             '&pageNo=' + str(page_num) + '&zcode=' + str(z))
    response = (url + 'ServiceKey=' + ServiceKey + '&numOfRows=1000' +
                '&pageNo=' + str(page_num))
    url_new = response.encode('utf-8')
    req = requests.get(url_new)
    bs = BeautifulSoup(req.text, 'html.parser')

    name = bs.findAll('statnm')
    stat_id = bs.findAll('statid')
    chger_id = bs.findAll('chgerid')

    charge_type = bs.findAll('chgertype')
    address = bs.findAll('addr')
    latitude = bs.findAll('lat')
    longitude = bs.findAll('lng')
    state = bs.findAll('stat')
    stat_upddt = bs.findAll('statupddt')
    lasttsdt = bs.findAll('lasttsdt')
    lasttedt = bs.findAll('lasttedt')

    nowtsdt = bs.findAll('nowtsdt')
    output = bs.findAll('output')
    method = bs.findAll('method')
    zcode = bs.findAll('zcode')
    limityn = bs.findAll('limitYn')
    limitdetail = bs.findAll('limitDetail')
    parking_free = bs.findAll('parkingfree')

    usetime = bs.findAll('usetime')
    busiid = bs.findAll('busiid')
    bnm = bs.findAll('bnm')
    businm = bs.findAll('businm')
    delyn = bs.findAll('delyn')
    deldetail = bs.findAll('deldetail')
    note = bs.findAll('note')

    total_num = str(bs.find('totalcount'))
    total = int(re.findall('\d+', total_num)[0])

    if page_num < total // 1000 + 1:
        for i in range(1000):
            names.append(name[i].text)
            stat_ids.append(stat_id[i].text)
            chger_ids.append(chger_id[i].text)
            charge_types.append(charge_type[i].text)
            addresss.append(address[i].text)
            latitudes.append(latitude[i].text)
            longitudes.append(longitude[i].text)
            states.append(state[i].text)
            stat_upddts.append(stat_upddt[i].text)  # *추가
            lasttsdts.append(lasttsdt[i].text)  # *추가
            lasttedts.append(lasttedt[i].text)  # *추가
            nowtsdts.append(nowtsdt[i].text)  # *추가
            outputs.append(output[i].text)
            methods.append(method[i].text)
            zcodes.append(zcode[i].text)
            usetimes.append(usetime[i].text)
            busiids.append(busiid[i].text)
            bnms.append(bnm[i].text)
            businms.append(businm[i].text)
            delyns.append(delyn[i].text)
            deldetails.append(deldetail[i].text)
            notes.append(note[i].text)
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
            stat_ids.append(stat_id[i].text)  # *추가
            chger_ids.append(chger_id[i].text)  # *추가
            charge_types.append(charge_type[i].text)
            addresss.append(address[i].text)
            latitudes.append(latitude[i].text)
            longitudes.append(longitude[i].text)
            states.append(state[i].text)
            stat_upddts.append(stat_upddt[i].text)  # *추가
            lasttsdts.append(lasttsdt[i].text)  # *추가
            lasttedts.append(lasttedt[i].text)  # *추가
            nowtsdts.append(nowtsdt[i].text)  # *추가
            outputs.append(output[i].text)
            methods.append(method[i].text)
            zcodes.append(zcode[i].text)
            usetime.append(usetime[i].text)
            busiid.append(busiid[i].text)
            bnm.append(bnm[i].text)
            businm.append(businm[i].text)
            delyn.append(delyn[i].text)
            deldetail.append(deldetail[i].text)
            notes.append(note[i].text)
            try:
                limityns.append(limityn[i].text)
                limitdetails.append(limitdetail[i].text)
            except:
                limityns.append('')
                limitdetails.append('')
            parking_frees.append(parking_free[i].text)

        break

# 시간마다 충전소 상태를 가져오게 만드는 함수


# def store_one_hour_state():
#     states = []
#     page_num = 1
#     while 1:
#         response = (url + 'ServiceKey=' + ServiceKey + '&numOfRows=1000' +
#                     '&pageNo=' + str(page_num) + '&zcode=' + str(z))
#         url_new = response.encode('utf-8')
#         req = requests.get(url_new)
#         bs = BeautifulSoup(req.text, 'html.parser')

#         state = bs.findAll('stat')

#         total_num = str(bs.find('totalcount'))
#         total = int(re.findall('\d+', total_num)[0])

#         if page_num >= total // 1000 + 1:
#             for i in range(total % 1000):
#                 states.append(state[i].text)
#             break

#         else:
#             for i in range(1000):
#                 states.append(state[i].text)
#             page_num += 1
#     states
#     return states


# 초기 데이터를 잘 받아왔는지 확인해보는 코드
final_data = pd.DataFrame([names, stat_ids, chger_ids, charge_types, addresss, latitudes, longitudes, usetimes, busiids, bnms, businms,
                           stat_upddts, lasttsdts, lasttedts, nowtsdts, outputs, methods, zcodes, limityns, limitdetails, parking_frees, delyns, deldetails, notes, states]).T
final_data.columns = ['충전소명', '충전소ID', '충전기ID', '충전타입', '주소', '위도', '경도', '이용가능시간', '기관아이디', '기관명', '운영기관명', '상태갱신일시', '최종충전시작', '최종충전종료', '충전중시작',
                      '출력', '충전방식', '지역코드', '이용자제한', '이용자제한사유', '무료 주차', '삭제여부', '삭제사유', '충전소안내', '실시간 상태(15분)']

save_path = os.getcwd()
final_data.to_csv(save_path + "/output/" + nowtext[:-2] + "00" + ".csv",
                  mode='w', encoding='utf-8-sig')
