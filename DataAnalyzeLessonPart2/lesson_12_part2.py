# 10.03.2025

import requests
from lxml import etree
url = 'https://bj.ke.com/ershoufang/'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}
res = requests.get(url,headers=headers)

tree = etree.HTML(res.text)
list_1 = tree.xpath('//ul[@class="clear"]')
count =  1
for e in list_1:
    title = e.xpath('.//a[@class="VIEWDATA CLICKDATA maidian-detail"]/text()')[0]
    addr = e.xpath('.//div[@class="positionInfo"]/a/text()')[0]
    # info = e.xpath('.//dic[@class="houseInfo"]/text()')[0]
    price = e.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()')[0]+'万'
    # unitprice = e.xpath('.//div[@class="unitPrice"]/span/text()')[0]
    print(count,title,addr,price)
    count += 1

