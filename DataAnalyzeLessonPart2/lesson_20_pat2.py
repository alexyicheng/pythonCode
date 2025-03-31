# 28.03.2025

import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randint(1,100,(4,4)),index=['小明', '小红', '小刚', '小美'],columns=['语文', '数学', '英语','化学'])

df['语文']['小明'] = 11
df['语文']['小刚'] = 16

# print(df.replace({11:12,13:55}))

# print(df['语文'].map({11:111}))

# print(df['语文'].map({11:21,13:23}))
df['测试'] = df['语文'].map(lambda x:x+10 )
# print(df)
df['passed or not'] = df['测试'].map(lambda x:'not passed' if x<60 else'passed')
# print(df)

def func(x):
    if x < 60:
        return 'not passed'
    elif x>=60 and x < 80:
        return 'good'
    else:
         return 'excellent'

df['matheLevel'] = df['数学'].map(func)
# print(df)

# print(df.rename({'语文':'abc'}))
print(df.rename({'语文':'Chinese'},axis=1))