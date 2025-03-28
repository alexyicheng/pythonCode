# 24.03.2025

import numpy as np
import pandas as pd

list1 = [1,2,3,4]
s = pd.Series(list1)

d = {
    'python':97,
    'java':88,
    'c++':70
}

p1 = pd.Series(d)
# print(p1)

# print(p1.python) = print(p1['python'])
# print(p1[['python','java']])
#
# print(p1.loc['python'])

# print(p1[0])
# print(p1[[0,1]])
# print(p1.iloc[0])
# print(p1.iloc[[0,2]])

print(p1[1:3])
print(p1.loc['python':'c++'])