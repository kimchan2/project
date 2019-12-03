#!/usr/bin/python
#_*_ coding:utf-8 _*_


# spri
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus


plusUrl = quote_plus(input('검색어를 입력하세요 : '))


# startDate

startDate = (input('시작날짜 입력(yyyy-mm-dd) : '))

# endDate
endDate = input('종료날짜 입력(yyyy-mm-dd) : ')


# pageNum
pageNum = 1


# pageCheck
count = 1

# url
url = f'https://spri.kr/search/ksearchAll?tar=1&srh=A&ord=N&dt=T&dt_fr={startDate}&dt_to={endDate}&os=&s={plusUrl}&page={pageNum}'


i = input('how many page crawling? : ')


lastPage = int(i)


while pageNum < lastPage+1:
   
    url = f'https://spri.kr/search/ksearchAll?tar=1&srh=A&ord=N&dt=T&dt_fr={startDate}&dt_to={endDate}&os=&s={plusUrl}&page={pageNum}'

   
    html = urlopen(url)
   
    soup = bs(html, "html.parser")
    
    print(f'---{count}page --------')

    

    title=soup.find_all('h4',class_='panel-title float-left')
    
    
    # print link & text
    for i in title:
        
        print(i.a.text)
        print(i.a.get('href'))




    


    pageNum += 1
    count += 1
 

