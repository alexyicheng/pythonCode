# 24.03.2025

import numpy as np
import pandas as pd

list1 = [1,2,3,4]
# s = pd.Series(list1)
# print(s)
n1 = np.array(list1)
s = pd.Series(n1)
# print(s.values)
# print(type(s.values))
s.index = ['a','b','c','d']
print(s)
print(s['d'])
print(s.d)
s.d = 44
print(s)

d = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
f = pd.Series(d)
print(f)