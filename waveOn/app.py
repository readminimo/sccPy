from flask import Flask, render_template, jsonify, request
import requests
import json
from pymongo import MongoClient

## 이건 뭘까ㅏ???
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta
response = requests.get(
    "http://www.khoa.go.kr/oceangrid/grid/api/buObsRecent/search.do?ServiceKey=lOofIbPo/oeXI6OjnfL76A==&ObsCode=TW_0062&ResultType=json")
data = response.json()

print(data)

# waves = {
#     'name': name,
#     'record_time': record_time,
#     'air_temp': air_temp,
#     'water_temp': water_temp,
#     'current_dir': current_dir
# }

# db.waveOn.insert_one(waves)

# print(record_time)

air_temp = data['result']['data']['air_temp']

# print(air_temp)

# html 가져오기

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
