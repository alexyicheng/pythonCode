import pandas as pd
import numpy as np

df_a = pd.DataFrame(np.random.randint(1, 100, (4,3)), index=['小明', '小红', '小刚', '小美'],
columns=['语文', '数学', '英语'])

df_b = pd.DataFrame(np.random.randint(1, 100, (4,3)), index=['小明', '小红', '小刚', '小美'],
columns=['语文', '数学', '英语'])

df_sum = df_a+df_b
print(df_sum)

df_add = df_a + 20
print(df_add)

s = pd.Series([10, 20, 30, 40],index = ['小明', '小红', '小刚', '小美'])

df_add_series = df_a.add(s,axis='index')
print(df_add_series)

def create_df(index,columns):
    data = []
    for i in index:
        ls = []
        for j in columns:
            ls.append(str(j)+str(i))
        data.append(ls)
    return pd.DataFrame(data,index=index, columns=columns)

df_1 = create_df([1,2,3],['A','B'])
df_2 = create_df([4,5],['A','B'])
#
df_concat_vertical = pd.concat([df_1,df_2],axis=0)
df_concat_horizontal = pd.concat([df_1,df_2],axis = 1)
print(df_concat_vertical)
print(df_concat_horizontal)

df_x = pd.DataFrame({
  '学号': ['001', '002', '003'],
  '姓名': ['张三', '李四', '王五'],
  '年龄': [18, 19, 20]
})

df_y = pd.DataFrame({
  '学号': ['002', '003', '004'],
  '成绩': [85, 90, 78]
})

print(pd.merge(df_x,df_y,on = '学号',how='inner'))
print( pd.merge(df_x, df_y, on='学号', how='outer'))
print( pd.merge(df_x, df_y, on='学号', how='left'))
print( pd.merge(df_x, df_y, on='学号', how='right'))

