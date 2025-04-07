import requests

page_num = input('please insert which page you want to visit')

url = f'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1743928792170&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=1&keyword=&pageIndex={page_num}&pageSize=10&language=zh-cn&area=de'

res = requests.get(url)
data = res.json()

for i in data['Data']['Posts']:
    print(i['RecruitPostName'])
    print(i['Responsibility'])
