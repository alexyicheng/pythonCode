import requests

page_num = 1
while True:
    url = f'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1743928792170&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=1&keyword=&pageIndex={page_num}&pageSize=10&language=zh-cn&area=de'

    res = requests.get(url)
    data = res.json()

    data_list = data['Data']['Posts']
    if data_list == None:
        break
    for i in data_list:
        print(i['RecruitPostName'])
        print(i['Responsibility'])
    print(f'current {page_num} page, get all data')
    page_num += 1