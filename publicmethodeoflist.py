# 27.11.2024

list_1 = [1,2,3,5,6,8,8,9]
# show the length of list
print(len(list_1))

# show the maximum of list
print(max(list_1))

# show the minimum of list
print(min(list_1))

# show every element of list_1
for element in list_1:
    print(element)

# show the position of element and value of list
for position,value in enumerate(list_1):
    # print('list_1[',position,']=',value)
    print(f'list_1[{position}]={value}')

# from list to set
set_1 = set(list_1)
print(set_1) # delete duplicates

lst1 = [12,3,4,5]
lst2 = [3,4,5]
# incorporation/union 2 list
print(lst1+lst2)

# kopy list
print(lst1*2)

# exist in list
print(12 in lst1)
if 12 in lst1:
    print('exist')
else:
    print('no exist')

# no exist in list
print(12 not in lst1)