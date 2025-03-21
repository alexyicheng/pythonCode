# 21.03.2025

ls = [10,20,30]
new_ls = []
for i in ls:
    new_ls.append(i-10)
print(new_ls)

import numpy as np

t1 = np.arange(10,40,10)
print(t1-10)


t2 = np.arange(24).reshape((4,6))
print(t2)
print('___________________')
t3 = np.arange(100,124).reshape((4,6))
print(t3)
print('___________________')
# print(t2+t3)
# print(t2-t3)
#
# t4 = np.arange(0,6)
# print(t4)
# print(t3-t4)

t5 = np.arange(4).reshape((4,1))
print(t5)
print('__________________________')
print(t3+t5)

t6 = np.arange(10)
# print(t3-t6) # error

'''
'''