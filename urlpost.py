# 27.10.2024

# user-agent -- again scraping

import random
from urllib.parse import quote,unquote
import requests


# UAlist = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15',
#     'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
# ]
# print(random.choice(UAlist))


# https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E9%97%AA%E8%80%80%E7%9A%84%E5%A5%B9&fenlei=256


# print(quote('性爱')) # decoding
# print(unquote('%E6%80%A7%E7%88%B1')) # encoding

# option 1
name = quote(input('please insert key-wort'))
url = f'https://www.baidu.com/s?wd={name}'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
print(res.content.decode())

# option 2
# url = 'https://www.baidu.com/s?'
# headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
# name = input('please insert key-wort')
# kw = {'wd':name}
# res = requests.get(url,headers=headers,params=kw)
# print(res.content.decode())




