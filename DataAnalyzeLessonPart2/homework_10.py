# 15.03.2025

import requests
from bs4 import BeautifulSoup
from DrissionPage import ChromiumPage

page = ChromiumPage()
url = 'https://www.mi.com/shop/category/list'
page.get(url)

divs = page.eles('.category-box')
# print(len(divs))

for div in divs:
    title = div.ele('.title').text.replace('','')
    # title = page.ele('x:./h2[@class="title"]')
    print(title)
    list_1 = div.eles('x:./ul[@class="category-list"]/li')
    for e in list_1:
        name = e.ele('.name').text
        print(name)