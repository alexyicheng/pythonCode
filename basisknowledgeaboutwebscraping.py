#25.10.2024

import requests

# 1.request web
# 2.request methode
# 3.fake - request header
# 4.request content - request body

# web scraping
# 1.confirm target - url
# 2.send request
# 3.take data - jsonpath/xpath/re
# 4.save data - (html,json,txt) database

# request methods
# get and post
# get -> ask ressource from web
# post -> give ressource to server

# User-Agent: fake normal web searcher
# cookie: keep log in
# referer: current request where is it from

# find url
url = 'https://www.baidu.com/'

# headers
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

# send request
# headers request format dictionary, request key,value
res = requests.get(url,headers=headers)

# save response
# res.encoding = 'utf-8'

# print(res.content.decode())
print(len(res.content.decode())) # length 2349

# the goal of adding user-agent is for fake request from browser not from python
# now is the length 412602


# with open('baidu.html','w',encoding='utf-8') as f:
#     f.write(res.content.decode())

# save picture
# url1 = 'https://wx1.sinaimg.cn/orj360/008p5Kk7ly1hqopny7gc0j30u01d6n3d.jpg'
# res1 = requests.get(url1)
# with open('sunqian.jpg','wb') as f:
#     f.write(res1.content)

# other property

# difference between res.text and res.content
# text: type str -> requests module decode from http headers code
# content : type bytes -> can decode()

