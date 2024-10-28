# 28.10.2024

import requests

# url = 'https://p1.music.126.net/IBVysj1VNv6K8M53JKPYzQ==/109951170084906221.jpg?imageView&quality=89'
# header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=header)
#
# with open('wangyiyunpic.jpg','wb') as f:
#     f.write(res.content)

url = 'https://tieba.baidu.com/f?'
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
res = requests.get(url,headers=header)
word = input('please insert Tieba name:')
page = int(input('please insert how much do pages you need:'))

for i in range(1,page):
    params = {
        'kw': word,
        'pn':i*50
    }
    res = requests.get(url,headers=header,params=params)

