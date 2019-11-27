#!/usr/bin/python
# _*_ coding:utf-8 _*_


import matplotlib.pyplot as plt
import naver_news
from wordcloud import WordCloud, STOPWORDS

#필요없는거같은데 일단 킵
#from PIL import Image,ImageDraw,ImageFont


#네이버 뉴스 헤드라인 크롤링
text = naver_news.i.attrs['title']


spwords=set(STOPWORDS) # 기본적으로 많이 쓰는 단어 (제외할 단어)
                       # ex)'should', "wouldn't", "how's", "i'm", 'then', etc ..

spwords.add(naver_news.plusUrl) #제외하고 싶은 단어 추가


# 워드 클라우드를 설정합니다.
#폰트:나눔명조 설치#http://cdn.naver.com/naver/NanumFont/fontfiles/NanumFont_TTF_ALL.zip

wordcloud = WordCloud(max_font_size=500, font_path='/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf',
        stopwords=spwords,
                     background_color='#FFFFFF',
                     width=1000,height=800).generate(text)

 
plt.figure(figsize=(8,5))
plt.imshow(wordcloud)#TODO
plt.tight_layout(pad=0)
plt.axis('off')

#워드클라우드 출력
plt.show()
#파일 다운로드
#plt.savefig('/home/ubuntu/wordcloud_image1.png', bbox_inches='tight')