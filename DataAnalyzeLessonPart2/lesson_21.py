import pandas as pd

data = {
    'name':['Alex','Dennis','Thomas','Alex','Dennis'],
    'Department':['Sales','Sales','Developer','Developer','Sales'],
    'Sale':[1000,1000,2100,1700,2300],
    'Month':['2024-01','2024-01','2024-01','2024-02','2024-02']
}

df = pd.DataFrame(data)
# print(df)

# print(df.groupby('name')['Sale'].sum())

# print(df.groupby('Department').agg({
#     'name':'count',
#     'Sale':'mean'
# }).rename(columns={'name':'Count of Employer','Sale':'AVG'}))

data_2 = {
    'name':['Thomas','Eileen','Jessica','Gerhard'],
    'age':[21,23,56,52]
}
df2 = pd.DataFrame(data_2)

bins =[20,30,40,50,60]
df2['Level']=pd.cut(data_2['age'],bins,right=False)
# print(df2)

data_3 = {
    'name':['Thomas','Eileen','Jessica','Gerhard'],
    'Salary':[3000,15000,5000,20000]
}
df3 = pd.DataFrame(data_3)
df3['salary_level'] = pd.qcut(df3['Salary'],3,labels=['level1','level2','level3'])
print(df3)