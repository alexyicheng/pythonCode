import requests


pagesite = input('Please insert the page you want to visit')
url = (f'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1741085895604&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=1&keyword=&pageIndex={pagesite}&pageSize=10&language=zh-cn&area=de')

if pagesite == 1:
    res = requests.get(url)
else:
    res = requests.get(url,params=pagesite)
print(res.text)
