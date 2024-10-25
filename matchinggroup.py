# 24.10.2024

import re

res = re.match(r'abc|ghl','abc')
# print(res.group())

res1 = re.match(r'.|\d','s234')
# print(res1.group())

# match group by (a|b)
res2 = re.match(r'\w*@(163|qq|126).com','abc@163.com')
# print(res2.group())

# res3 = re.match(r'<(\w*)>.*</\1>','<html>login</html>')
res3 = re.match(r'<(\w*)><(\w*)>.*</\2></\1>','<html><body>login</body></html>')
# print(res3.group())
# option 2
res4 = re.match(r'<(?P<L1>\w*)><(?P<L2>\w*)>.*</(?P=L2)></(?P=L1)>','<html><body>login</body></html>')
# print(res4.group())

# match website
li = ['www.baidu.com','www.python.org','http.jd.cn','www.py.en','www.abc.cn']
# res5 = re.match(r'www(\.)\w*\1(com|org|cn)','www.baidu.com')
# print(res5.group())

# for i in li:
#     res5 = re.match(r'(www|http)\.\w*\.(com|org|cn)', i)
#     if res5:
#         print(res5.group())
#     else:
#         print(f'{i} this web goes wrong')

# next level

# search() return only the first element which matched
res6 = re.search(r'\d','py5th3on')
# print(res6.group())

# findall() return alle element which machted
res7 = re.findall(r'\d','asdb52145asdf10025796')
# print(res7)
# print(type(res7))

# sub(pattern,repl,string,count)
# pattern -> content
# repl -> new element
# string -> string
# count -> how much time
res8 = re.sub(r'alex','python','hello alex')
# print(res8)

res9 = re.sub(r'\d','2','That is the 30th day in the month',1)
# print(res9)

res10 = re.split(r',','hello,python,java,c,c++,php',3)
# print(res10)

# greedy match
res11 = re.match('m*','mmmmmm')
# print(res11.group())

# ungreedy match
res12 = re.match('m?','mmmmm') # use ? return only once matched element
print(res12.group())

