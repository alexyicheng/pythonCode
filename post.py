# 28.10.2024

import requests

# post request

# get - request params
# post - request data

url = ''

header = {
    'user-agent':'',
    'cookie':''
}

post_data = {

}

res = requests.get(url,headers=header,data=post_data)
print( res.content)