#!/usr/bin/python
# _*_ coding:utf-8 _*_

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from urllib import parse



# 보안뉴스 검색 후 검색 결과
# 보안뉴스는 euc-kr 사용

# 검색어 받기
plusUrl = input('검색어를 입력하세요 : ')

# 보안뉴스 url받기
plusUrl = 'https://www.boannews.com/search/news_list.asp?search=title&find=' + plusUrl
# url파싱
search = parse.urlparse(plusUrl)

# 쿼리 파싱
query = parse.parse_qs(search.query)  # 보안뉴스 인코딩 값이 euc-kr

# 쿼리값 인코딩
S_query = parse.urlencode(query, encoding='euc-kr', doseq=True)  # URL 인코딩


url = "https://www.boannews.com/search/news_list.asp?{}".format(S_query)


# 페이지수
pageNum = 1


# 페이지 체크
count = 1

# url
url = "https://www.boannews.com/search/news_list.asp?{}".format(S_query) + "&Page=" + str(pageNum)


i = input('몇 페이지를 크롤링 할까요? : ')


lastPage = int(i)
while pageNum < lastPage + 1:

    url = "https://www.boannews.com/search/news_list.asp?{}".format(S_query) + "&Page=" + str(pageNum)
    html = urlopen(url)
    soup = bs(html, "html.parser")

    
    # 조건에 맞는 파일을 다 출력해라
    title = soup.find_all('span', class_='news_txt')

    print(f'---{count}페이지 결과입니다 --------')
    for i in title:
        print(i.text)

    pageNum += 1
    count += 1
