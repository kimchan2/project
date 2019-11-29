!/usr/bin/python
# _*_ coding:utf-8 _*_

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.now()
now_date = now.strftime('%Y.%m.%d')
one_year_before = now - relativedelta(years=1)
one_year_before_date = one_year_before.strftime('%Y.%m.%d')

# 네이버 검색 후 검색 결과
plusUrl = quote_plus(input('검색어를 입력하세요 : '))

# 시작날짜
startDate = (now_date)
# 종료날짜
endDate = (one_year_before_date)

# 페이지수
pageNum = 1

# 페이지 체크
count = 1

# url
url = f'https://search.naver.com/search.naver?&where=news&query={plusUrl}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds={startDate}&de={endDate}&docid=&nso=so:r,p:from20191101to20191125,a:all&mynews=0&cluster_rank=30&start={pageNum}&refresh_start=0'

lastPage = 3991 # naver_news provides only 4,000 articles

while pageNum < lastPage + 1:
    url = f'https://search.naver.com/search.naver?&where=news&query={plusUrl}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds={startDate}&de={endDate}&docid=&nso=so:r,p:from20191101to20191125,a:all&mynews=0&cluster_rank=30&start={pageNum}&refresh_start=0'
    html = urlopen(url)
    soup = bs(html, "html.parser")

    # 조건에 맞는 파일을 다 출력해라
    title = soup.find_all(class_='_sp_each_title')

    print(f'---{count}페이지 결과입니다 --------')
    for i in title:
        print(i.attrs['title'])
    pageNum += 10
    count += 1
