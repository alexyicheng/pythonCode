# 10.03.2025

import requests
from lxml import etree

url = 'https://bgm.tv/anime/browser?sort=rank'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'

tree = etree.HTML(res.text)

list_name = tree.xpath('.//div[@class="inner"]//a/text()')
list_info = tree.xpath('.//p[@class="info tip"]/text()')
# print(list_info
list_rank = tree.xpath('.//small[@class="fade"]/text()')
# print(list_rank)
list_rating = tree.xpath('.//span[@class="tip_j"]/text()')
data = []
for name,info,rank,rating in zip(list_name,list_info,list_rank,list_rating):
    item = {
        'name' : name.strip(),
        'info': info.strip(),
        "rank": rank.strip(),
        "rating": rating.strip()
    }
    data.append(item)
for e in data:
    print(e)

