# 07.03.2025

# Goal:scrawler Data from eastmoney.com

import requests
import json
import re

url = 'https://push2ex.eastmoney.com/getTopicZTPool?cb=callbackdata3716714&ut=7eea3edcaed734bea9cbfc24409ed989&dpt=wz.ztzt&Pageindex=0&pagesize=20&sort=fbt%3Aasc&date=20250307&_=1741359093088'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

res = requests.get(url,headers=headers)

# option 1
# data_string = res.text
# # print(type(data))
# json_match = re.search(r'\((\{.*\})\)', data_string)
# result = {}
# if json_match:
#     json_data = json.loads(json_match.group(1))  # Parsen als JSON
#     # option 1
#     # Extrahiere alle Werte von "n"
#     # result = {entry["c"]: entry["n"] for entry in json_data["data"]["pool"]}
#     # print(result)
#     # option 2
#     for e in json_data['data']['pool']:
#         result[e['c']] = e['n']
#     print(result)

# option 2

text = res.text
# change format of text callbackdata
new_text = re.findall(r'callbackdata\d+\((.*?)\);',text)[0]
# change string in json format
dict_data = json.loads(new_text)
# get the data of json
for e in dict_data['data']['pool']:
    id = e['c']
    name = e['n']
    print(id,name)