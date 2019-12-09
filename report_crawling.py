#!/usr/bin/python
#_*_ coding:utf-8 _*_

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus, quote
from datetime import datetime
#from dateutil.relativedelta import relativedelta
import pymysql
import math

conn = pymysql.connect(host='localhost', user='user_name', password='userpassword', db='crawling', charset='utf8mb4')
cur = conn.cursor()

industry = ['클라우드', 'AI', '5G', '스마트팩토리', '블록체인']
def store(industry, title, URL, date, writer):
    cur.execute(
        "INSERT INTO Report(industry, title, URL, date, writer) VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\")", (industry ,title, URL, date, writer)
    )
    cur.connection.commit()

cur.execute("USE crawling")
pageNum = 0
industry_count = 0;
page_count = 1
for i in industry:
    while 1:
        url = f'https://www.itfind.or.kr/report/analysis/list.do?rangeTarget=createDate&searchTarget=all&searchText={quote(i)}&pageSize=10&pageIndex={pageNum}'
        html = urlopen(url)
        soup = bs(html, "html.parser")

        print(f'--------{i}---{page_count}페이지 결과입니다 --------')
        title = soup.find_all('td', class_='tit')
        writer = soup.find_all('td', class_='writer')
        date = soup.find_all('td', class_='date')

        page = soup.find("div", {"class": "total"})
        infoPrint = []
        for a in page.find_all("strong"):
            info = a.get_text()
            infoPrint.append(info)

        last_page = math.trunc(int(infoPrint[0]) / 10) + 1
        print(last_page)

        for j,k,l in zip(title, date, writer):
            print(j.a.text)
            print("https://www.itfind.or.kr/" + j.a.get('href'))
            URL = "https://www.itfind.or.kr/" + j.a.get('href')
            text = j.a.text
            DATE = k.text
            WRITER = l.text
            store(i, text, URL, DATE, WRITER)
            
        pageNum += 1
        page_count += 1

        if pageNum == last_page:
            pageNum = 0
            page_count = 1
            break

cur.close()
conn.close()