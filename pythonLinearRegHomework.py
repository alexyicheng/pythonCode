import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv('boston_housing_data.csv')

# print(df.head(5))

X=df.drop(columns='MEDV')
y=df['MEDV']
print(df.isnull().sum())
print(df['MEDV'].fillna(0,inplace=True))
print(df.isnull().sum())

line=LinearRegression()

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

line.fit(X_train,y_train)
print("权重:",line.coef_)
print("截距:",line.intercept_)

Y = line.predict(X_test)
print("预测值",Y)
print("真实值",y_test)

plt.figure(figsize=(15,6))
plt.rcParams['font.family']='SimHei'
plt.plot(y_test,label='真实值',color='red',marker='o')
plt.plot(Y,label='预测值',color='yellow',marker='D')
plt.xlabel('预测集序号')
plt.ylabel('数据值')
plt.legend()
plt.show()