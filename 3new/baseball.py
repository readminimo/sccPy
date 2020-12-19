import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo')

soup = BeautifulSoup(data.text, 'html.parser')

league = soup.select('#regularTeamRecordList_table > tr')

for team in league:
     rank = team.select_one('th > strong').text
     name = team.select_one('.tm > div > span').text
     point = team.select_one(':nth-child(7) > strong').text

     if point > '0.5':
        print(rank, name, point)

