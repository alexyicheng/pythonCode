# 03.06.2025

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

data = pd.read_csv('boston.csv')
# print(data.head(5))

X = data.iloc[:,:-1]
y = data.iloc[:,-1]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.25,random_state=0)
regressor = DecisionTreeRegressor(max_depth=9)
regressor.fit(X_train,y_train)
print(regressor.score(X_train,y_train))
print(regressor.score(X_test,y_test))

train_score=[

]
test_score= [

]
for depth in range(1,13):
    tree = DecisionTreeRegressor(random_state=0,max_depth=depth)
    tree.fit(X_train,y_train)
    train_score.append(tree.score(X_train,y_train))
    test_score.append(tree.score(X_test,y_test))
plt.figure(figsize=(10,5))
plt.plot(train_score,marker='o',c='red',label='Training')
plt.plot(test_score,marker='o',c='green',label='Testing')
plt.legend()
plt.show()
