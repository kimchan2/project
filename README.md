# Industry Gate
---------------

## 1. Industry Gate란
------------------

### 1.1 Industry Gate 소개
-----------------
 정보통신기술의 뉴스기사 헤드라인을 통해 산업의 동향을 알아보고,
 핵심키워드를 단어구름으로 추출해내며, 관련 산업의 보고서를 출력하는 웹사이트이다.

### 1.2 사용한 도구
---------------
1. BeatifulSoup : 파이썬에서 웹 크롤러로 사용, 네이버뉴스, ITFIND에서 보고서를 크롤링 해옴
2. WordCloud : 크롤링한 네이버 뉴스 제목을 워드클라우드로 보여줌
3. Google Cloud Natural Language API : 크롤링한 네이버 뉴스 제목의 감정 분석을 통해 해당 산업의 긍정, 부정을 나타냄

## 2. 준비사항
---------------
1. Ubuntu 18.04 LTS, APACHE, MySQL, PHP
 - 웹서버
2. Google Cloud Natural Language API 키
 - 가이드라인 : https://cloud.google.com/natural-language/docs/basics?hl=ko

## 3. 설치
----------
1. python3 가상환경 구성

`sudo pip3 install virtualenv`

`virtualenv 가상환경이름`

`source 가상환경이름/bin/activate`


 
