#!/usr/bin/python
# _*_ coding:utf-8 _*_

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from urllib import parse



# 정보통신정책연구원 검색 후 검색 결과
# 인코딩 euc-kr 사용

# 검색어 받기
plusUrl = input('검색어를 입력하세요 : ')

#  정보통신정책원  url받기
plusUrl = 'http://www.kisdi.re.kr/kisdi/jsp/fp/kr/search/search.jsp?strQuery=' + plusUrl
# url파싱
search = parse.urlparse(plusUrl)

# 쿼리 파싱
query = parse.parse_qs(search.query)  # 정보통신정책원 인코딩 값이 euc-kr=보안뉴스


# 쿼리값 인코딩
S_query = parse.urlencode(query, encoding='euc-kr', doseq=True)  # URL 인코딩


url = "http://www.kisdi.re.kr/kisdi/jsp/fp/kr/search/search.jsp?{}".format(S_query)+"&strCate=publication"


# 시작날짜

startDate = (input('시작날짜 입력(yyyy-mm-dd) : '))

# 종료날짜
endDate = (input('종료날짜 입력(yyyy-mm-dd) : '))





# 페이지수
pageNum = 0


# 페이지 체크
count = 1




# url
url = url +  "&iStartCount=" + str(pageNum)+"&S&strStartTime="+startDate+"&strEndTime="+endDate

print(url)

i = input('몇 페이지를 크롤링 할까요? : ')


lastPage = int(i)
while pageNum < lastPage*10 - 9:

    url = url
   
    html = urlopen(url)
    soup = bs(html, "html.parser")

    
    # 조건에 맞는 파일을 다 출력해라
    title = soup.find_all('dt')

    print(f'---{count}페이지 결과입니다 --------')
    for i in title:
        print(i.text)
        print("http://www.kisdi.re.kr"+i.a.get('href'))

    pageNum += 10
    count += 1
