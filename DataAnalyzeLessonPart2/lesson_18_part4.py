import pandas as pd
import numpy as np

d = {
    'name':['coco','Dennis','Laura'],
    'age':[18,21,25]
}

df = pd.DataFrame(d)

# print(type(df.values))
# print(df.values)
# print(df.columns)
# print(df.index)
# print(df.shape)
print(df.head())

df.index = ['a','b','c']
print(df)

df.columns = ['aa','bb']
print(df)

p1 = pd.DataFrame(d,index=list('abc'))
print(p1)

# df = pd.DataFrame(np.random.randint(10,100,(4,6)))
df = pd.DataFrame(np.random.randint(10,100,(4,6)),index=['a','b','c','d'],columns=['python','java','web','numpy','pandas','C++'])
print(df)
# print(df[['python','java']])
#
# print(df.loc['a'])
# print(df.iloc[1])

print(df.loc[['a','b']])
print(df.iloc[[0,1]])

print(df.loc['a']['python'])
print(df.loc['a','python'])
print(df.loc['b'][1])
print(df.iloc[0]['java'])
print(df.iloc[0][1])
print(df.iloc[0,1])

print(df['a':'c'])

print(df.loc[:,'python':'web'])
print(df.iloc[1:3,1:3])
print(df.loc['a':'c','java':'web'])

print(df.loc['a','python':'web'])