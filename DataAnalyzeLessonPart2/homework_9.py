# 12.03.2025


import requests
from bs4 import BeautifulSoup

url = 'https://www.youlai.cn/dise/'
res = requests.get(url)

bs = BeautifulSoup(res.text,'lxml')
# select all data von dt, with value <a>
a_all = bs.select('dt>a')
count = 1
for a in a_all:
    print(count,a.text)
    # get the link of <a href>
    details = a.get('href')
    # define new url
    detail_url = f'https://www.youlai.cn{details}'
    # call new url
    detail_res = requests.get(detail_url)
    d_bs = BeautifulSoup(detail_res.text,'lxml')
    print(d_bs)
    p_all = d_bs.select('.dise_info_02 p')
    for p in p_all:
        print(p.text.replace('\n',''))
    print('__________________________')
    count += 1





