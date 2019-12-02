#!/usr/bin/python
# _*_ coding:utf-8 _*_

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
import os





#google natural language
# 네이버 검색 후 검색 결과
plusUrl = quote_plus(input('검색어를 입력하세요 : '))

# 시작날짜

startDate = (input('시작날짜 입력(yyyy.mm.dd) : '))

# 종료날짜
endDate = (input('종료날짜 입력(yyyy.mm.dd) : '))


# 페이지수
pageNum = 1


# 페이지 체크
count = 1

# url
url = f'https://search.naver.com/search.naver?&where=news&query={plusUrl}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds={startDate}&de={endDate}&docid=&nso=so:r,p:from20191101to20191125,a:all&mynews=0&cluster_rank=30&start={pageNum}&refresh_start=0'


i = input('몇 페이지를 크롤링 할까요? : ')


lastPage = int(i) * 10 - 9

while pageNum < lastPage + 1:
    url = f'https://search.naver.com/search.naver?&where=news&query={plusUrl}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds={startDate}&de={endDate}&docid=&nso=so:r,p:from20191101to20191125,a:all&mynews=0&cluster_rank=30&start={pageNum}&refresh_start=0'
    html = urlopen(url)
    soup = bs(html, "html.parser")

    # 조건에 맞는 파일을 다 출력해라
    title = soup.find_all(class_='_sp_each_title')


    #print(url)
    #print(f'---{count}페이지 결과입니다 --------')
    for i in title:

        news=  i.attrs['title'].replace("‘"," ").replace("’"," ").replace("“"," ").replace("”"," ").replace("'"," ").replace('"'," ").replace("\n","")

        print(news)
        #Google natural language// api발급받아야됨..    
        curl="curl " + "\"https://language.googleapis.com/v1/documents:analyzeSentiment?key={APIKEY}\" " +" -s -X POST -H"  + " \"Content-Type:application/json\" " +"--data " +"'{" + "\"document\""+":"+"{" + "\"type\""+":"+ "\"PLAIN_TEXT\""+","+"\"content\""+":\"" + news + "\"}"+"}"+ "'"



        #system명령어
        os.system(curl )


    pageNum += 10
    count += 1








