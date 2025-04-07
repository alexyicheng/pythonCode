# 04.04.2025

import requests

tieba_name = input('please insert the tieba name')
url = f'https://tieba.baidu.com/f?kw={tieba_name}'

res = requests.get(url)
print(res.text)
