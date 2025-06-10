# 03.06.2025

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

X,y = load_iris(return_X_y=True)
X = X[:,:2]
# print(X)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)
tree = DecisionTreeClassifier(max_depth=6)
tree.fit(X_train,y_train)
Y = tree.predict(X_test)
print('Vorhersage:',Y)
print(tree.score(X_train,y_train))
print(tree.score(X_test,y_test))
print('overview',classification_report(y_test,Y))


train_score=[

]
test_score= [

]
for depth in range(1,13):
    tree = DecisionTreeClassifier(random_state=0,max_depth=depth)
    tree.fit(X_train,y_train)
    train_score.append(tree.score(X_train,y_train))
    test_score.append(tree.score(X_test,y_test))
plt.figure(figsize=(10,5))
plt.plot(train_score,marker='o',c='red',label='Training')
plt.plot(test_score,marker='o',c='green',label='Testing')
plt.legend()
plt.show()