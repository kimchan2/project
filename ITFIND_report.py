#!/usr/bin/python
#_*_ coding:utf-8 _*_

# ITFIND
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus


# 검색어
plusUrl = quote_plus(input('검색어를 입력하세요 : '))


# 시작날짜

startDate = (input('시작날짜 입력(yyyy-mm-dd) : '))

# 종료날짜
endDate = input('종료날짜 입력(yyyy-mm-dd) : ')


# 페이지수
pageNum = 0


# 페이지 체크
count = 1

# url
url = f'https://www.itfind.or.kr/report/analysis/list.do?rangeTarget=createDate&rangeBeginDate={startDate}&rangeEndDate={endDate}&searchTarget=all&searchText={plusUrl}&pageSize=10&pageIndex={pageNum}'


i = input('몇 페이지를 크롤링 할까요? : ')


lastPage = int(i)


while pageNum < lastPage:
   
    url = f'https://www.itfind.or.kr/report/analysis/list.do?rangeTarget=createDate&rangeBeginDate={startDate}&rangeEndDate={endDate}&searchTarget=all&searchText={plusUrl}&pageSize=10&pageIndex={pageNum}'
   
    html = urlopen(url)
   
    soup = bs(html, "html.parser")
    
    #링크출력

    print(f'---{count}페이지 결과입니다 --------')

    

    title=soup.find_all('td',class_='tit')
    
    
    # 조건에 맞는 파일을 다 출력해라
    for i in title:
        
        print(i.a.text)
        print("https://www.itfind.or.kr/"+i.a.get('href'))




    


    pageNum += 1
    count += 1
 

