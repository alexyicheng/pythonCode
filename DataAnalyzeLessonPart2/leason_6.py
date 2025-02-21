# 21.02.2021

import random

# ls = [1,2,3]
# for i in ls:
#     print(i)
#
# t_1 = (1,2,3)
# for i in t_1:
#     print(i)
#
# t = 'abcdefg'
# for string in t:
#     print(string)

# d = {'name':'Eileen','Geschlecht':'W'}
# for i in d:
#     print(i)
#     print(d[i])
#
# for key,value in d.items():
#     print(key,':',value)

# num = random.randint(1,100)
# for i in range(10):
#     num_input = int(input('geben sie einer Zahl ein'))
#     if num == num_input:
#         print('gut geratten')
#         break
#     elif num > num_input:
#         print('zu klein')
#     else:
#         print('zu groß')


# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(3):
#     for j in range(4):
#         print(i,j)

# ls = [[1,2,3],[5,6,7]]
# for i in ls:   # [1,2,3],[5,6,7]
#     for j in i:
#         print(j) # 1,2,3,5,6,7

for x in range(1,10):
    for y in range(1,x+1):
        print(f'{x}x{y}={x*y}',end='   ')
    print()