# 10.03.2025

import requests
from lxml import etree
count = 1
for page in range(1,4):
    url = f'https://bgm.tv/anime/browser?sort=rank&{page}'
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'

    tree = etree.HTML(res.text)

    # option 1
    # list_name = tree.xpath('.//div[@class="inner"]//a/text()')
    # list_info = tree.xpath('.//p[@class="info tip"]/text()')
    # # print(list_info
    # list_rank = tree.xpath('.//small[@class="fade"]/text()')
    # # print(list_rank)
    # list_rating = tree.xpath('.//span[@class="tip_j"]/text()')
    # data = []
    # for name,info,rank,rating in zip(list_name,list_info,list_rank,list_rating):
    #     item = {
    #         'name' : name.strip(),
    #         'info': info.strip(),
    #         "rank": rank.strip(),
    #         "rating": rating.strip()
    #     }
    #     data.append(item)
    # for e in data:
    #     print(e)

    # option 2
    list_1 = tree.xpath('//ul[@id="browserItemList"]/li')
    for e in list_1:
        # .// 夫循环里面的子循环
        title = e.xpath('.//a[@class="l"]/text()')[0]
        detail_url = e.xpath('.//a[@class="l"]/@href')
        info = e.xpath('.//p[@class="info tip"]/text()')[0]
        info= info.replace('\n','').replace(' ','')
        fade = e.xpath('.//small[@class = "fade"]/text()')[0]
        num = e.xpath('.//span[@class="tip_j"]/text()')[0]
        print(count,title,info,fade,num)
        detail_url = f'https://bgm.tv/{detail_url}'
        d_res = requests.get(detail_url,headers=headers)

        count +=1