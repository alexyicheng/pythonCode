# 21.03.2025

import numpy as np

t = np.arange(1,17).reshape((4,4))
print(t)

# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]

# print(t[0])
# print(t[-1])

# print(t[0][1]) # first row second column
# print(t[0,1]) # first row second column
# print(t[2,2])

# print(t[0,0:4]) # start:end
# # [1 2 3 4]
# print(t[1:4,1:3])
# # [[ 6  7]
# #  [10 11]
# #  [14 15]]
# print(t[1:,1:])
# # [[ 6  7  8]
# #  [10 11 12]
# #  [14 15 16]]
# print(t[0,0:4:2]) # step 2
# #[1 3]
t[1,1] = 66
print(t)

t_2 = np.arange(10)
print(t_2)
# [0 1 2 3 4 5 6 7 8 9]
# print(t_2>5)
# [False False False False False False  True  True  True  True]
print(t_2[t_2>5])
# [6 7 8 9]

t_3 = np.array(['a','b','c'])
print(t_3[t_3=='a'])
# ['a']

t_5 = np.array([1,2,3,4,5,6])
t_6 = np.array([7,8,9,10,0,1])
t_7 = np.array([True,False,True,False,True,False])

print(np.where(t_7,t_6,t_5))

t8 = np.arange(1,10)
print(t8)
print(np.where(t8%2==1,100,50))

# and  &
# or |
# not ~

t9 = np.random.randint(1,11,(3,4))
print(t9)
# print(t9[t9>5])
# print(t9[t9<5]) # print(t9[~(t9>5)])
# print(t9<5)
# print(t9[~(t9>5)]) # print(t9[t9<5])

# take greater than 5 and less than 8
print(t9[(t9>5) & (t9<8)])

# take 5 or less than 8
print(t9[(t9==5)|(t9<8)])