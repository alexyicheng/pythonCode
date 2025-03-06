import requests

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

url = 'https://www.bkchina.cn/product/productList'

ls = ['season','ham','snack','dessert','meats','coffee','breakfirst','happy_meal']

for i in ls:
    cs = {'type':i}
    res = requests.post(url,data=cs,headers=headers)
    data = res.json()

    # option 1
    # for a in data:
    #     for b in data[a]:
    #     print(b['FName'])

    # option 2
    for key,value in data.items():
        # proof the current value is null or not
        # 家庭餐: null
        # option 1
        # if value != None:
        # option 2
        if value is not None:
            for e in value:
                print(e['FName'])