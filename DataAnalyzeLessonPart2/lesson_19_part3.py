import pandas as pd

def make_df(index,columns):
    data = []
    for i in columns:
        ls = []
        for j in index:
            ls.append(str(j)+str(i))
        data.append(ls)
        return pd.DataFrame(data,index=index,columns= columns)

df1 = make_df([1,2],['a','b'])
df2 = make_df([3,4],['a','b'])
print(pd.concat([df1,df2]))

print(pd.concat([df1,df2],axis=1))


df3 = make_df([1,2,3,4],['a','b','c','d'])
df4 = make_df([2,3,4,5],['b','c','d','e'])
print(df3)
print(df4)
print(pd.concat([df3,df4]))
print(pd.concat([df3,df4],join='inner'))


d = {
    'name':['Alex','Thomas','Olaf'],
    'id':['1','2','3'],
    'age':['18','19','20']
}

df5 = pd.DataFrame(d)

d2 = {
    'id':['2','3','4'],
    'gender':['m','m','m'],
    'title':['student','inter','Developer']
}

df6 = pd.DataFrame(d2)
print(df6)
print(df5)
print(pd.merge(df5,df6))
print(pd.merge(df5,df6,left_index = True,right_index=True))