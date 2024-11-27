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

