#13.10.2024

import requests
from bs4 import BeautifulSoup
import re

wz = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
url = 'https://book.zongheng.com/showchapter/1330288.html'
res = requests.get(url,headers=wz)

soup = BeautifulSoup(res.text,'lxml')
lis = soup.findAll('li',class_='col-4')

for l in lis:
    a = l.find('a')
    adress = a.get('href')
    title = a.text

    res1 = requests.get(adress,headers=wz)
    soup1 = BeautifulSoup(res1.text, 'lxml')
    content1 = soup1.find_all('div',class_='content')[0]
    # content2 = content1.find('p')
    text = '\n'.join(content1.stripped_strings)
    #print(text)
    open(f'78!重生/{title}.txt','w',encoding='utf-8').write(text)