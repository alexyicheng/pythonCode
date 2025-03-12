# 12.03.2025

from bs4 import BeautifulSoup
import requests


url = f'https://bgm.tv/anime/browser?sort=rank'
headers = {
       'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
bs = BeautifulSoup(res.text,'lxml')
# print(bs.title.text)
# print(bs.find('title').text)
# print(bs.find_all('title')[0].text)
# print(bs.select('head>title')[0].text)


# option 1
# print(len(bs.select('#browserItemList>li')))
# option 2
# print(len(bs.select('.browserFull>li')))

list_1 = bs.select('#browserItemList>li')
for e in list_1:
    a_tag = e.find('a',class_='l')
    title = a_tag.text
    p_tag = e.find('p',class_='info tip')
    info = p_tag.text
    info = info.replace('\n','').replace(' ','')
    small_tag = e.find('small',class_='fade')
    fade = small_tag.text
    span_tag = e.find('span',class_='tip_j')
    num = span_tag.text
    detail = a_tag.get('href')
    detail_url = f'https://bgm.tv/{detail}'
    d_res = requests.get(detail_url,headers=headers)
    d_res.encoding = 'utf-8'
    d_bs = BeautifulSoup(d_res.text,'lxml')
    div_tag = d_bs.find('div',id = "subject_summary")
    print(detail_url, title, info, fade, num)
    print(div_tag.text)
    print('______________________________________________________________')

