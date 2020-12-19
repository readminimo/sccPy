import requests

response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

city_air = response_data.json()

# print(city_air['RealtimeCityAir']['row'][0]['NO2'])
# 모든 구의 PM10 값을 찍어주자
guPm10 = city_air['RealtimeCityAir']['row']

for gu in guPm10:
    # PM10 값이 20 미만인 구만 찍어주자!
    if gu['PM10'] < 15:
         print(gu['MSRSTE_NM'], gu['PM10'])

# gu_infos = city_air['RealtimeCityAir']['row']
#
# for gu_info in gu_infos:
#     print(gu_info['MSRSTE_NM'], gu_info['PM10'])