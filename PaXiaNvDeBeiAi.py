# 18.10.2024
import requests
from bs4 import BeautifulSoup
import re
page = 1
while page < 44:
    wz = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
    url = f'http://www.tzy2.com/read/144051_{page}.html'
    res = requests.get(url,headers=wz)
    soup = BeautifulSoup(res.text,'lxml')
    lis = soup.findAll('div',class_='chapter')
    for l in lis:
        content = l.text
        print(f'downloading{page} website={url}')
        open(f'侠女的悲哀/Capital-{page}.txt', 'w',encoding='utf-8').write(content)
    page += 1
