import numpy as np
import pandas as pd

# d = {
#     'python':97,
#     'java':88,
#     'c++1':70,
# 'c++2':70,
# 'c++3':70,
# 'c++4':70,
# 'c++5':70,
# }
# p1 = pd.Series(d)
# print(p1)
# print(p1.shape)
# print(p1.size)
# # standard 5 element
# print(p1.head()) # first 5 element
# print(p1.tail()) # last 5 element

# s = pd.Series(['Alex','Thomas','Angela',np.nan])
# print(s.isnull())
# print(pd.isnull(s))
# print(s.notnull())
# print(pd.notnull(s))

# print(s[~s.isnull()])
# print(s[s.notnull()])

s1 = pd.Series(np.random.randint(10,100,3))
s2 = pd.Series(np.random.randint(10,100,4))
print(s1)
print(s1+10)
print(s1+s2) # not the same length NaN
print(s1.add(s2,fill_value=0)) #