import requests

url = 'https://www.bkchina.cn/product/productList'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}
cs = {
    'type':'ham'
}
# res = requests.post(url,data=cs,headers=headers)
# res_data = res.json()

# option 1
# gwzx = res_data['国王臻选']
# for i in gwzx:
#     print(i['FName'])
# jdxl = res_data['经典系列']
# for i in jdxl:
#     print(i['FName'])
# czxl = res_data['超值系列']
# for i in czxl:
#     print(i['FName'])

# option 2
# for i in res_data:
#     for j in res_data[i]:
#         print(j['FName'])

# option 3
# for key,value in res_data.items():
#     for i in value:
#         print(i['FName'])

list_1 = [
    'season','ham','snack','dessert','meats','coffee','breakfirst','happy_meal'
]
for i in list_1:
    cs = {'type':i}
    res = requests.post(url, data=cs, headers=headers)
    res_data = res.json()
    for key,value in res_data.items():
        if value is not None:
            for j in value:
                print(j['FName'])