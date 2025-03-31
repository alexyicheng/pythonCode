# 28.03.2025

import pandas as pd
import numpy as np

n = np.array([1,2,3,np.nan,5,6])

# print(np.sum(n))
# print(np.nansum(n)) # extract nan

df = pd.DataFrame(np.random.randint(1,100,(5,5)),columns=list('abcde'))
df.loc[2,'b']=np.nan
df.loc[3,'b'] = None
print(df)

# axis = 0 means column axis = 1 means row
# s = df.isnull().any(axis = 1)
# print(s)
# print(~s)
# print(df[~s])

# s = df.notnull().all(axis = 1)
# print(df[s])

s = df.isnull().any()
# print(s)
# print(~s)
# print(df.loc[:,~s])

# print(df.fillna(method = 'pad'))
# print(df.fillna(method = 'bfill'))

df_a = pd.DataFrame(np.random.randint(1, 100, (4,3)), index=['小明', '小红', '小刚', '小美'],
columns=['语文', '数学', '英语'])
print(df_a)
df_a.loc['小明'] = df_a.loc['小红']
print(df_a)
# True means duplicate
print(df_a.duplicated())
print(df_a.duplicated(keep='first'))
print(df_a.duplicated(keep='last'))
print(df_a.drop_duplicates())
