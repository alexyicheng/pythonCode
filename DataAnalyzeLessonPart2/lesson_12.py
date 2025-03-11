# 10.03.2025

import requests
from lxml import etree

url = 'https://bgm.tv/anime/browser?sort=rank'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'

# print(res.text)

tree = etree.HTML(res.text)

print(tree.xpath('/html/head/title'))
print(tree.xpath('//title'))