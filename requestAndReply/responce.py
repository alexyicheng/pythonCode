# 04.04.2025

import requests

url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1743771806510&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=de'

res = requests.get(url)

data = res.json()

text = ''
for i in data['Data']['Posts']:
    print(i['RecruitPostName'])
    print(i['Responsibility'])
    text += i['RecruitPostName']+'\n'
    text += i['Responsibility']+'\n'

with open('tencent.csv','w',encoding='utf-8') as f:
    f.write(text)