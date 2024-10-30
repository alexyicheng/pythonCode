# 24.10.2024

import re

res = re.match('Alex','Alex is the coolest person on the world')
# print(res)
# print(res.group ())

res1 = re.match('..','Hello Python')
# print(res1.group())

# match string
# option 1
# res2 = re.match('[He]...','Hello Python')
# print(res2.group())
# option 2
res2 = re.match('[a-zA-Z]...','Hello Python')
# print(res2.group())

# match Number
# option 1
# res3 = re.match('[0-9]','5236')
# print(res3.group())
# option 2 with string with number
res4 = re.match(r'.\d','a5236s')
# print(res4.group())

# match everything without number
res5 = re.match(r'\D..','<5213')
# print(res5.group())

# match space tab
res6 = re.match(r'\s\sh','  hello')
# print(res6.group())

# match everything without space,tab
res7 = re.match(r'\S','<hahaha')
# print(res7.group())

# match a-z,A-Z,0-9,_,
res8 = re.match(r'\w','Alex')
# print(res8.group())

# * match before string 0 time or multi times
res9 = re.match(r'\w*','coolcool.')
# print(res9.group())

# + match before string 1 time or multi times
res10 = re.match(r'<h4>(.+)</h4>','<h4>Ihr Profil</h4>')
print(res10.group())

# ? match before string 1 time or 0 time
res11 = re.match(r'\w?','12Hello')
# print(res11)