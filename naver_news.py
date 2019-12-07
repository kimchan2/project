#!/usr/bin/python
# _*_ coding:utf-8 _*_

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from datetime import datetime
from dateutil.relativedelta import relativedelta
import requests
import pymysql
import os
import json


conn = pymysql.connect(host='localhost', user='user_name', password='userpassword', db='crawling', charset='utf8mb4')
cur = conn.cursor()

now = datetime.now()
now_date = now.strftime('%Y.%m.%d')
one_year_before = now - relativedelta(years=1)
three_month_before = now - relativedelta(months=3) # 감정분석은 3개월전까지만
one_month_before = now - relativedelta(months=1)
one_year_before_date = one_year_before.strftime('%Y.%m.%d')
one_month_before_date = one_month_before.strftime('%Y.%m.%d')
three_month_before_date = three_month_before.strftime('%Y.%m.%d')

def store(title, score, magnitude):
    cur.execute(
        "INSERT INTO cloud(title, score, magnitude) VALUES (\"%s\", \"%s\", \"%s\")", (title, score, magnitude)
    )

def store_only_title(title):
    cur.execute(
        "INSERT INTO cloud(title) VALUES (\"%s\")", (title)
    )
    cur.connection.commit()

plusUrl = quote_plus(input('검색어를 입력하세요 : ')) # 네이버 검색
cur.execute("USE crawling")
start_date = (now_date) # 오늘날짜
end_date = (one_month_before_date) # 오늘로부터 1달전 날짜
last_date = (one_year_before_date) # 오늘로부터 1년전 날짜
three_date = (three_month_before_date)
page_num = 1 # 페이지수
count = 1 # 페이지 체크

last_page = 3991 # naver_news provides only 4,000 articles = 3991
while 1:
    page_num = 1  # 페이지 초기화
    count = 1  # 카운트 초기화

    while page_num < last_page + 1:

        #url
        url = f'https://search.naver.com/search.naver?&where=news&query={plusUrl}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds={end_date}&de={start_date}&docid=&nso=so:r,p:from20191101to20191125,a:all&mynews=0&cluster_rank=30&start={page_num}&refresh_start=0'
        html = urlopen(url)
        soup = bs(html, "html.parser")

        # 조건에 맞는 파일을 다 출력
        title = soup.find_all(class_='_sp_each_title')

        print(f'---{end_date}~{start_date}뉴스 중{count}페이지 결과입니다 --------')
        for i in title:
            news = i.attrs['title'].replace("‘", " ").replace("’", " ").replace("“", " ").replace("”", " ").replace("'", " ").replace('"', " ").replace("\n", "")
            print(i.attrs['title'])
            if start_date > three_date: # 감정분석은 3개월전까지만
                curl = "curl " + "\"https://language.googleapis.com/v1/documents:analyzeSentiment?key=API키\" " + " -s -X POST -H" + " \"Content-Type:application/json\" " + "--data " + "'{" + "\"document\"" + ":" + "{" + "\"type\"" + ":" + "\"PLAIN_TEXT\"" + "," + "\"content\"" + ":\"" + news + "\"}" + "}" + "'"
                #os.system(curl)
                i = os.popen(curl).read()
                i = json.loads(i)
                store(news, i["documentSentiment"]["score"], i["documentSentiment"]["magnitude"])
            else:
                store_only_title(news)
        page_num += 10
        count += 1

        if page_num > last_page+1:
            one_day_before = one_month_before - relativedelta(days=1) # end_date - 1일
            one_day_before_date = one_day_before.strftime('%Y.%m.%d')
            one_month_before = one_month_before - relativedelta(months=1)  # 한달전 날짜에서 한달전을 뺌
            one_month_before_date = one_month_before.strftime('%Y.%m.%d')  # YYYY.MM.DD로 저장
            start_date = one_day_before_date  # 시작 날짜는 end_date-1로 바꿈
            end_date = one_month_before_date  # end_date는 한달전 날짜로 바꿈

        if end_date < last_date:
            break
    if end_date < last_date:
        break

cur.close()
conn.close()