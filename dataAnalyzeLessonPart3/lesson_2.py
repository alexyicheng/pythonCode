# 16.05.2025

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from sklearn.metrics import roc_curve,auc,roc_auc_score
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

cancer = datasets.load_breast_cancer()
# print(cancer)

X = cancer.data
y = cancer.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)

log=LogisticRegression()
log.fit(X_train,y_train)
Y = log.predict(X_test)
# print('prediction: ',Y)

plt.figure(figsize=(20,5))
plt.plot(y_test,marker='o',ls = '', c = 'red',label='real')
plt.plot(Y,marker='o',ls = '', c = 'green',label='predict')
plt.legend()
plt.xlabel('样本序号')
plt.ylabel('类别')
# plt.show()

matrix = confusion_matrix(y_true=y_test,y_pred=Y)
print(matrix)

class_name = ['malignant','benign']
plt.figure(figsize=(8,6))
cm = confusion_matrix(y_test,Y)
sns.heatmap(cm,annot=True,xticklabels=class_name,yticklabels=class_name,cmap=plt.cm.RdYlGn,fmt='d',alpha = 0.6)


print('accuracy: ',accuracy_score(y_test,Y))
print('prediction: ',precision_score(y_test,Y))
print('recall: ',recall_score(y_test,Y))
print('f1',f1_score(y_test,Y))

y2 = np.array([1,1,0,1,0,1])
scores = np.array([0.8,0.6,0.3,0.4,0.5,0.7])
fpr,tpr,thresholds = roc_curve(y_true=y2,y_score=scores,pos_label=1)
print(fpr)
print(auc(fpr,tpr))
print(roc_auc_score(y_true=y2,y_score=scores))

# ROC

y_prob=log.predict_proba(X_test)[:,1]
fpt,tpr,thresholds= roc_curve(y_test,y_prob)
print(fpr)
roc_auc=auc(fpt,tpr)
print(roc_auc)

plt.figure(figsize=(8,6))
plt.plot([0,0,1],[0,1,1],lw=2,ls='-',label = 'prefect prediction')
plt.plot(fpr,tpr,color='orange',lw=2,label='roc_auc')
plt.plot([0,1],[0,1],lw=2,)