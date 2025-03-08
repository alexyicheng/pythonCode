# 08.03.2025
# save multi picture

import requests
import re
import json

url = 'https://image.so.com/j?callback=jQuery18309530312362155853_1741447996303&q=%E5%9B%BE%E7%89%87&qtag=&pd=1&pn=60&correct=%E5%9B%BE%E7%89%87&adstar=0&tab=all&sid=2ee56843817677e60cdcf91d638f451c&ras=6&cn=0&gn=0&kn=50&crn=0&bxn=20&cuben=0&pornn=0&manun=24&src=tab_www&sn=130&ps=125&pc=125&_=1741448151636'
res = requests.get(url)
# JSONDecodeError means current data donot like dictionary or list
# jQuery18309530312362155853_1741447996303({});
# print(res.json())
# solution
text = res.text
# replace the beginning and end jQuery18309530312362155853_1741447996303({})
# text_new = text.replace('jQuery18309530312362155853_1741447996303(','').replace(');','')
# \d+ means mutli numbers (.*?) all string and number
text_new = re.findall(r'jQuery\d+_\d+\((.*?)\);',text)[0]
# from str -> dict
dict_data = json.loads(text_new)

count = 1
for i in dict_data['list']:
    img_url = i['img'] # get img url
    print(img_url)
    img_res = requests.get(img_url)
    with open(f'pic/{count}.png','wb') as f:
        f.write(img_res.content)
    count += 1

