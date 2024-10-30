# 30.10.2024

import json

data = [{'name':'Alex','age':23},{'name':'Daniela','age':21},{'name':'Günter','age':30}]
# ensure_ascii decode the language string like öüä or other language string like chinese
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

# from string to json
s = '[{"name":"DreamFollower","age":32}]'
l = json.loads(s)
print(type(l))
print(l)

# change list to dictionary
for i in l:
    print(type(i))

