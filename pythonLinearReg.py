# 09.05.2025

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

iris = load_iris()

X = iris.data[:,2].reshape(-1,1)
y = iris.data[:,3]

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
# plt.show()

print('均方误差',mean_squared_error(y_test,Y))
print('平均绝对误差',mean_absolute_error(y_test,Y))
print('r2分数训练集',r2_score(y_train,line.predict(X_train)))
print('r2分数测试集',r2_score(y_test,Y))
print(line.score(X_train,y_train))
print(line.score(X_test,y_test))


