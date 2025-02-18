# 17.02.2025

# tupel
t = (1,2,3)

# print(t[::2])
# print(len(t))
print(t.index(3))
# how many times is 3 in the tuple
print(t.count(3))

# dictionary
# key:value

d = {'name':'Dennis'}
print(d['name'])
print(d.get('names','Daniela'))

# add element into dictionary
d['age'] = 16
print(d)

d['age'] = 21
print(d)

# delete element
del d['age']
print(d)

stadtlist  = {'Region':['Herford','Enger']}
stadtlist['Region'].append('Spenge')
stadtlist['Region'].append('Bünde')
stadtlist['Region'].remove('Enger')
print(stadtlist)
print(stadtlist['Region'][1])

list_1  = {'Person Info':{'Name':'Ruwe','Age':18,'Gender':'Man'}}
print(list_1)
print(list_1['Person Info']['Name'])
list_1['Person Info']['Hobby'] = ['KTV','Casino']
print(list_1)

dict_1 = {'15':[{'name':'Eileen'},{'name':'Alex'},{'name':'Gerhard','exam':98}]}
print(dict_1['15'][2]['exam'])

# set
# unique value without duplicates
s_1 = {1,2,3,4,2,2,1}
s_1.add('D')
print(s_1)
s_1.remove(2)
print(s_1)
print(s_1.pop())
s_1.update({8,5,7})

print(s_1)
# empty set
print(type(set()))