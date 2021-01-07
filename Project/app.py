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
# db.waveOn.insert_one(data)

record_time = data['result']['data']['record_time']
air_temp = data['result']['data']['air_temp']
water_temp = data['result']['data']['water_temp']
current_dir = data['result']['data']['current_dir']
name = data['result']['meta']['obs_post_name']
waves = {
    'name': name,
    'record_time': record_time,
    'air_temp': air_temp,
    'water_temp': water_temp,
    'current_dir': current_dir
}

db.waveOn.insert_one(waves)

print(record_time)

air_temp = data['result']['data']['air_temp']

print(air_temp)

## html 가져오기
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
#
# ##
#
# @app.route('/test', methods=['GET'])
# def test_get():
#     title_receive = request.args.get('title_give')
#     print(title_receive)
#     return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})
#
#
# @app.route('/test', methods=['POST'])
# def test_post():
#     title_receive = request.form['title_give']
#     print(title_receive)
#     return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})
#
#
#
#
# @app.route('/show', methods=['POST'])
# def write_time():
#     time = {
#         'record_time': record_time
#     }
#
#     db.waveOn.insert_one(time)
#
#     return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)
