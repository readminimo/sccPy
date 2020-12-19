
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##
find = db.movies.find_one({'title': '월-E'})

# print(find)
# print(find['star'])

wall = find['star']
#  월이의 평점과 같은평점 ! 을 변수에 넣어 사용

find_same = list(db.movies.find({'star': wall}))

# many와 list의 차이
# 리스트에 접근할 때 반복문을 사용하여 , 또는 배열 하나씩 [0] 접근.

for movie in find_same:
    print(movie['title'], movie['rank'])
    db.movies.update_many({'star': wall}, {'$set': {'star': 0}})
    print("수정",movie['title'], "star:",movie['star'])
# 업데이트용