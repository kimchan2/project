#!/usr/bin/python
# _*_ coding:utf-8 _*_

# posco management labortory

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus


# plusUrl
plusUrl = quote_plus(input('input keyword : '))


# startdate

startDate = (input('startDate(yyyy.mm.dd) : '))

# enddate
endDate = input('endDate(yyyy.mm.dd) : ')


# pageNumber
pageNum = 1


# pageCount
count = 1

# url
url = f'https://www.posri.re.kr/ko/board/thumbnail/list/63?stDate={startDate}&edDate={endDate}&type=all&text={plusUrl}&perpage=20&order=regdate%20desc&page={pageNum}'


i = input('how many page crawling? : ')

lastPage = int(i)


while pageNum < lastPage+1:

    url = f'https://www.posri.re.kr/ko/board/thumbnail/list/63?stDate={startDate}&edDate={endDate}&type=all&text={plusUrl}&perpage=20&order=regdate%20desc&page={pageNum}'

    html = urlopen(url)

    soup = bs(html, "html.parser")

    # print

    print(f'---{count}page --------')

    title = soup.find_all('h4')

    # print for title
    for i in title:

        print(i.a.text)
        print("https://www.posri.re.kr"+i.a.get('href'))

    pageNum += 1
    count += 1
