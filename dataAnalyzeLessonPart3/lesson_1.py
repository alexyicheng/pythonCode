# 15.05.2025

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

iris = load_iris()
# print(iris)

# step 1: eigenvalue
iris['data']
# print(iris['data'])

# step 2: get goal column
iris['target']
# print(iris['target'])

# step 3: merge
# print(np.concatenate([iris.data,iris.target.reshape(-1,1)],axis=1))

# step 4: transform data into table
data = np.concatenate([iris.data,iris.target.reshape(-1,1)],axis=1)
data = pd.DataFrame(data,columns=['sepal_length (cm)', 'sepal_width (cm)', 'petal_length (cm)', 'petal_width (cm)','type'])
# print(data)

# step 5: get frequency
ps = data['type'].value_counts()
pl=ps/len(data)

# step 6: visualize Data
sns.countplot(x='type',data=data)
# plt.show()

# mean = data['sepal_length (cm)'].mean()
# median = data['sepal_length (cm)'].median()
# print('average: ',mean)
# print('median: ',median)
# mode = data['sepal_length (cm)'].mode()
# print('mode: ',mode.iloc[0])

# plt.rcParams['font.family']='SimHei'
# plt.rcParams['font.size']=15
# plt.figure(figsize=(8,6))
# sns.histplot(data['sepal_length (cm)'],kde=True)
# plt.axvline(mean,ls='-',c='orange',label='average')
# plt.axvline(median,ls='-',c='red',label='median')
# plt.axvline(mode.iloc[0],ls='-',c='green',label='mode')
# plt.legend()
# plt.show()

x = [1,4,6,10,22,18,33]
# option 1
# print(np.quantile(x,q=[0.25,0.5,0.75]))
# # option 2
# print(np.percentile(x,q=[25,50,75]))
# option 3 with pandas
s = pd.Series(x)
# print(s.describe())
#
# df = pd.DataFrame([[93,98,89],[94,95,91],[93,93,93]],index=['li','wang','zhang'],columns=['math','chinese','english'])
# print(df.sum(axis=1))
# print(df.var(axis=1))

plt.figure(figsize=(10,6))
t1=np.random.randint(1,11,size=100)
t2=np.random.randint(11,21,size=500)
t3=np.concatenate([t1,t2])

t4=np.random.randint(1,11,size=500)
t5=np.random.randint(11,21,size=100)
t6=np.concatenate([t4,t5])

left_skew=pd.Series(t3)
sns.kdeplot(left_skew,fill=True,label='left')
right_skew=pd.Series(t6)
sns.kdeplot(right_skew,fill=True,label='right')

plt.legend()
plt.show()