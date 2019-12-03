#!/usr/bin/python
# _*_ coding:utf-8 _*_

# ITFIND
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from urllib import parse

# 검색어
plusUrl = quote_plus(input('검색어를 입력하세요 : '))


# 시작날짜

startDate = (input('시작날짜 입력(yyyy-mm-dd) : '))

# poscoreport format
startDate2 = (input('시작날짜 입력(yyyy.mm.dd) : '))

# 종료날짜
endDate = input('종료날짜 입력(yyyy-mm-dd) : ')

# poscoreport format
endDate2 = (input('종료날짜 입력(yyyy.mm.dd) : '))


# itfind,kisdiPageNumstart=0// seri,postco=1
pageNum = 0

# 페이지 체크
count = 1


i = input('몇 페이지를 크롤링 할까요? : ')


lastPage = int(i)


while pageNum < lastPage:
    # itfind
    url = f'https://www.itfind.or.kr/report/analysis/list.do?rangeTarget=createDate&rangeBeginDate={startDate}&rangeEndDate={endDate}&searchTarget=all&searchText={plusUrl}&pageSize=10&pageIndex={pageNum}'

    html = urlopen(url)

    soup = bs(html, "html.parser")

    # 링크출력

    print(f'---{count}page itfind --------')

    title = soup.find_all('td', class_='tit')

    # itifind
    # 조건에 맞는 파일을 다 출력해라
    for i in title:

        print(i.a.text)
        print("https://www.itfind.or.kr/"+i.a.get('href'))

    # spri
    url = f'https://spri.kr/search/ksearchAll?tar=1&srh=A&ord=N&dt=T&dt_fr={startDate}&dt_to={endDate}&os=&s={plusUrl}&page={pageNum+1}'

    html = urlopen(url)

    soup = bs(html, "html.parser")

    print(f'---{count}page spri --------')

    title = soup.find_all('h4', class_='panel-title float-left')

    # print link & text
    for i in title:

        print(i.a.text)
        print(i.a.get('href'))

    # posco

    url = f'https://www.posri.re.kr/ko/board/thumbnail/list/63?stDate={startDate2}&edDate={endDate2}&type=all&text={plusUrl}&perpage=20&order=regdate%20desc&page={pageNum+1}'

    html = urlopen(url)

    soup = bs(html, "html.parser")

    # print

    print(f'---{count}page --------posco')

    title = soup.find_all('h4')

    # print for title
    for i in title:

        print(i.a.text)
        print("https://www.posri.re.kr"+i.a.get('href'))

    pageNum += 1
    count += 1

# ksidi


pageNum = 0
#  정보통신정책원  url받기
plusUrl = 'http://www.kisdi.re.kr/kisdi/jsp/fp/kr/search/search.jsp?strQuery=' + plusUrl
# url파싱
search = parse.urlparse(plusUrl)
# 쿼리 파싱
query = parse.parse_qs(search.query)  # 정보통신정책원 인코딩 값이 euc-kr=보안뉴스
# 쿼리값 인코딩
S_query = parse.urlencode(query, encoding='euc-kr', doseq=True)  # URL 인코딩

# 페이지 체크
count = 1

# url

url = "http://www.kisdi.re.kr/kisdi/jsp/fp/kr/search/search.jsp?{}".format(
    S_query)+"&strCate=publication"


while pageNum < lastPage*10 - 9:

    url = url + "&iStartCount=" + \
        str(pageNum)+"&S&strStartTime="+startDate + \
        "&strEndTime="+endDate+"&strSort=date"

    html = urlopen(url)
    soup = bs(html, "html.parser")

    # 조건에 맞는 파일을 다 출력해라
    title = soup.find_all('dt')

    print(f'---{count}ksidi --------')
    for i in title:
        print(i.text)
        print("http://www.kisdi.re.kr"+i.a.get('href'))

    pageNum += 10
    count += 1
