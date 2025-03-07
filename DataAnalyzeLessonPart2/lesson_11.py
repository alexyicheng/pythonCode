# 07.03.2025

import requests
# global request
url = 'https://join.qq.com/api/v1/position/searchPosition?timestamp=1741369080023'
# request department
department_url = 'https://join.qq.com/api/v1/dictionary/?timestamp=1741369078033&types=RecruitType,BusinessGroup,RecruitProjectPostList'
department_res = requests.get(department_url)
department_data = department_res.json()
# define dictionary to save the info about department from other request
department_dict = {}
for i in department_data['data']['RecruitProjectPostList']:
    department_name = i['name']
    department_id = i['code']
    # dictionaryname[key] = [value]
    department_dict[department_id] = department_name

# request payload
# option 1
# data = '{"projectIdList":[2,12,1,14,20,5],"keyword":"","bgList":[],"workCountryType":0,"workCityList":[],"recruitCityList":[],"positionFidList":[],"pageIndex":1,"pageSize":10}'
# headers = {
#     'content-type':'application/json;charset=UTF-8'
# }
# res = requests.post(url,data=data,headers=headers)
# print(res.json())

# option 2
data_2 = {
    "projectIdList":[2,12,1,14,20,5],
    "keyword":"",
    "bgList":[],
    "workCountryType":0,
    "workCityList":[],
    "recruitCityList":[],
    "positionFidList":[],
    "pageIndex":1,
    "pageSize":10
}
res_2 = requests.post(url,json=data_2)
res_data = res_2.json()

# extract data
for i in res_data['data']['positionList']:
    title = i['positionTitle']
    city = i['workCities']
    projectname = i['projectName']
    position = i['positionFamily']
    # join info over html
    print(title + ','+ department_dict[str(position)] + ',' + city + ',' + projectname )

