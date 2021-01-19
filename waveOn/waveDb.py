import requests
import json
from pymongo import MongoClient

client = MongoClient('mongodb://test:test@3.34.4.14', 27017)
db = client.dbsparta

obs_post_ids = ['TW_0062', 'TW_0093', 'TW_0091', 'TW_0069', 'TW_0071', 'HB_0002', 'HB_0003', 'TW_0062',
                'TW_0090', 'TW_0092', 'HB_0001']

for obs_post_id in obs_post_ids:
    # obs_post_id = 'TW_0062'
    # url = "http://www.khoa.go.kr/oceangrid/grid/api/buObsRecent/search.do?ServiceKey=lOofIbPo/oeXI6OjnfL76A==&ObsCode=TW_0062&ResultType=json"
    url = "http://www.khoa.go.kr/oceangrid/grid/api/buObsRecent/search.do?ServiceKey=lOofIbPo/oeXI6OjnfL76A==&ObsCode=" + obs_post_id + "&ResultType=json"
    response = requests.get(url)
    data = response.json()
# print(data)

    name = data['result']['meta']['obs_post_name']
    long = data['result']['meta']['obs_lon']
    lat = data['result']['meta']['obs_lat']
    obs_post_id = data['result']['meta']['obs_post_id']

    record_time = data['result']['data']['record_time']
    air_temper = data['result']['data']['air_temp']
    water_temp = data['result']['data']['water_temp']
    current_dir = data['result']['data']['current_dir']
    wave_height = data['result']['data']['wave_height']

    waves = {
        'obs_post_id': obs_post_id,
        'name': name,
        'lat': lat,
        'long': long,
        'record_time': record_time,
        'air_temp': air_temper,
        'water_temp': water_temp,
        'current_dir': current_dir,
        'wave_height': wave_height
            }
    db.waveOn.insert_one(waves)
    print(waves)


