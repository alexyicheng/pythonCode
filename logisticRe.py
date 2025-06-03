
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import warnings

warnings.filterwarnings('ignore')

iris=load_iris()
X,y = iris.data,iris.target
print(X)
X=X[y!=0,2:]
print(X)
y=y[y!=0]

y[y==1]=0
y[y==2]=1

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

lg = LogisticRegression()

lg.fit(X_train,y_train)
Y = lg.predict(X_test)
print(lg.score(X_test,y_test))

