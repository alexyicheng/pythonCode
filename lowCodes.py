# 27.11.2024

# short,single codes

# too much line -> not classy
# new_list = []
# for i in range(0,10):
#     new_list.append(i)
# print(new_list)

# 1 line style
new_list = [x for x in range(0,10)]
print(new_list)

# create list with all even number from 0 to 10
# even_list = []
# for x in range(0,10):
#     if x%2 == 0:
#         even_list.append(x)
# print(even_list)
even_list = [x for x in range(0,10) if x%2 == 0]
print(even_list)

# create dictionary -> key: 1-5, value: number to power of 2
# new_dict = {}
# for i in range(1,6):
#     new_dict[i] = i**2
# print(new_dict)
new_dict = {x: x**2 for x in range(1,6)}
print(new_dict)

# combine 2 list into 1 dictionary
list_key = ['name','age','gender'] # define key
list_value = ['Sophia',20,'woman'] # define value
# dict_person = {}
# for x in range(0,len(list_key)): # 0 1 2
#     # combine the element of lists into key and value of dictionary
#     dict_person[list_key[x]] = list_value[x]
# print(dict_person)
dict_person = {list_key[x] : list_value[x]  for x in range(0,len(list_key))}
print(dict_person)

price_laptop = {'MBP':286,'HP':125,'Dell':201,'Lenovo':199,'acer':99}
top_laptop = { key:value for key,value in price_laptop.items() if value >= 200 }
print(top_laptop)

list_1 = [1,2,3,3,4]
# create set insert the element of list_1 to power 2
set_1 = { i**2 for i in list_1}
print(set_1) # {16, 1, 4, 9}