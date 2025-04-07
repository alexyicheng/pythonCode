# 04.04.2025

import requests

url = 'https://img2.baidu.com/it/u=3561205914,3812723719&fm=253&fmt=auto&app=120&f=JPEG?w=800&h=1120'

res = requests.get(url)
# res.encoding = 'utf-8'
# print(res.content)

with open('sunqian.png','wb') as f:
    f.write(res.content)
