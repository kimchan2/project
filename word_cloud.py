#!/usr/bin/python
# _*_ coding:utf-8 _*_

from bs4 import BeautifulSoup as bs
from konlpy.tag import *
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pymysql
import itertools

conn = pymysql.connect(host='localhost', user='user_name', password='userpassword', db='crawling', charset='utf8mb4')
cur = conn.cursor()
cur.execute("USE crawling")
cur.execute("SELECT title FROM Cloud")
result = cur.fetchall()

cur.close()
conn.close()

result = list(itertools.chain.from_iterable(result)) # 튜플을 리스트로 변환

okt = Okt()

sentences_tag = []
for sentence in result:
    morph = okt.pos(sentence)
    sentences_tag.append(morph)

noun_adj_list = []
for sentence1 in sentences_tag:
    for word, tag in sentence1:
        if tag in ['Noun', 'Adjective']:
            noun_adj_list.append(word)

counts = Counter(noun_adj_list)
tags = counts.most_common(20)

wc = WordCloud(max_font_size=500, font_path='/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf',
                    background_color='white',
                    width=1000, height=800)

cloud = wc.generate_from_frequencies(dict(tags))

plt.figure(figsize=(8, 5))
plt.imshow(cloud)
plt.axis('off')
plt.tight_layout(pad=0)

plt.show()