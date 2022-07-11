import requests

url = 'http://apis.data.go.kr/B553530/TRANSPORTATION/ELECTRIC_CHARGING'
params = {'serviceKey': 'WQ3OLgIT9KBQOZ1kOrn1hS5akC+uhQzyXiisG75us6v0XxTW03gCZNINODnPBpMrfuLNH2BG4bOG8B9QOo8A8g==',
          'pageNo': '1', 'numOfRows': '10', 'apiType': 'xml', 'q1': '울산광역시', 'q2': '중구'}

response = requests.get(url, params=params)
print(response.content)
