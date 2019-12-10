# Industry Gate
---------------

웹사이트 주소: http://52.141.16.225/ig.php

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

## 3. 설치 및 실행
----------
1. python3 가상환경 구성

`sudo pip3 install virtualenv`

`virtualenv 가상환경이름`

`source 가상환경이름/bin/activate`

2. python3 라이브러리 설치

`pip3 install beautifulsoup4`

`pip3 install wordcloud`

`pip3 install quote`

`pip3 install datetime`

`pip3 install pymysql`

`pip3 install matplotlib`

`pip3 install konlpy` 

3. MySQL 설치 및 설정

`sudo apt install mysql-client`

`sudo apt install mysql-server`

`sudo mysql -u root -p`

`ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';`

`CREATE DATABASE crawling;`

`CREATE USER 'user_name'@'localhost' IDENTIFIED BY 'userpassword';`

`GRANT ALL PRIVILEGES ON crawling.* to user_name@localhost;`

`FLUSH PRIVILEGES;`

`CREATE TABLE cloud( id int(7) NOT NULL AUTO_INCREMENT PRIMARY KEY,
		     title varchar(200) NOT NULL,
		     score decimal(2,1),
		     magnitude decimal(2,1),
		     created TIMESTAMP DEFAULT CURRNET_TIMESTAMP);`

`CREATE TABLE report( id int(7) NOT NULL AUTO_INCREMENT PRIMARY KEY,
		      industry varchar(200) NOT NULL,
		      title varchar(200) NOT NULL,
		      URL varchar(333) NOT NULL,
		      created TIMESTAMP DEFAULT CURRENT_TIMESTAMP);`

4. 크롤링 실행

`python3 naver_news.py`

`python3 report_crawling.py`

`python3 word_cloud.py`
