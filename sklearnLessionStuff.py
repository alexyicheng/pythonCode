# 21.11.2024
from statistics import correlation

# sklearn Methods

# linearRegression
from sklearn.linear_model import LinearRegression
import numpy as np

# data x = input y = target
x = np.array([[1,2],[2,3],[4,5],[6,7]])
y = np.array([3,5,9,13])

# create Model of LinearRegression
model = LinearRegression()

# simulate
model.fit(x,y)

print(f'intercept: ,{model.intercept_}')
print(f'coef: ,{model.coef_}')

# prediction
y_pred = model.predict(np.array([[7,8]]))
print(f'prediction: ,{y_pred}')

# Logistic Regression
from sklearn.linear_model import LogisticRegression

x = np.array([[1,2],[2,3],[4,5],[6,7]])
y = np.array([0,0,1,1])

model = LogisticRegression()

model.fit(x,y)

# prediction
y_pred = model.predict(np.array([[7,8]]))
print(f'prediction: {y_pred}')

# K-Nearest Neighbors (KNN)
from sklearn.neighbors import KNeighborsClassifier

x = np.array([[1,2],[2,3],[4,5],[6,7]])
y = np.array([0,0,1,1])

model = KNeighborsClassifier(n_neighbors=3)

model.fit(x,y)

y_pred = model.predict(np.array([[7,8]]))
print(f'prediction: {y_pred}')

# Support Vector Machine (SVM)
from sklearn.svm import SVC

x = np.array([[1,2],[2,3],[4,5],[6,7]])
y = np.array([0,0,1,1])

model = SVC()

model.fit(x,y)

y_pred = model.predict(np.array([[7,8]]))
print(f'prediction: {y_pred}')

# Decision Tree

from sklearn.tree import DecisionTreeClassifier

x = np.array([[1,2],[2,3],[4,5],[6,7]])
y = np.array([0,0,1,1])

model = DecisionTreeClassifier()

model.fit(x,y)

y_pred = model.predict(np.array([[7,8]]))
print(f'prediction: {y_pred}')

# Random Forest
from sklearn.ensemble import RandomForestClassifier

x = np.array([[1,2],[2,3],[4,5],[6,7]])
y = np.array([0,0,1,1])

# create random 100 random forest models
model = RandomForestClassifier(n_estimators=100)

model.fit(x,y)

y_pred = model.predict(np.array([[7,8]]))
print(f'prediction: {y_pred}')

# Naive Bayes

from sklearn.naive_bayes import GaussianNB


x = np.array([[1,2],[2,3],[4,5],[6,7]])
y = np.array([0,0,1,1])

model = GaussianNB()

model.fit(x,y)

y_pred = model.predict(np.array([[7,8]]))
print(f'prediction: {y_pred}')

# K-Means Clustering
from sklearn.cluster import KMeans

x = np.array([[1,2],[2,3],[4,5],[6,7]])
y = np.array([0,0,1,1])

model = KMeans(n_clusters=2)

model.fit(x,y)

y_pred = model.predict(np.array([[7,8]]))
print(f'prediction: {y_pred}')

# Principal Component Analysis (PCA)
import numpy as np
from sklearn.decomposition import PCA

x = np.array([[1,2,3],
             [4,5,6],
             [7,8,9],
             [10,11,12]])

pca = PCA(n_components=2)

# simulate PCA model and take data into new Area
x_pca = pca.fit_transform(x)

print(f'Data after transform: {x_pca}')

print(f'main matrix: {pca.components_}')

print(f'explain function : {pca.explained_variance_ratio_}')

# Descriptive Statistics
import numpy as np

data = np.array([1,2,3,4,5,6,7,8,9,10])

mean = np.mean(data)
std_dev = np.std(data)
range_ = np.ptp(data)
median = np.median(data)

print(f'median:{mean},average:{std_dev},minimum:{range_},median:{median}')

# Correlation Analysis
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

correlation_ = np.corrcoef(x,y)[0,1]

print(f'perterson correlation: {correlation_}')

# T-Test
from scipy import stats

data1 = [2,3,4,5,6]
data2 = [3,4,5,6,7]

t_stat, p_value = stats.ttest_ind(data1,data2)
print(f'T:{t_stat},P:{p_value}')

# Analysis of Variance (ANOVA)
from scipy import stats

group1 = [2,3,4,5,6]
group2 = [3,4,5,6,7]
group3 = [4,5,6,7,8]

f_stat, p_value = stats.f_oneway(group1,group2,group3)
print(f'F:{f_stat},P:{p_value}')

# Time Series Analysis

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

data = [112,118,132,129,121,135,148,148,136,119]

series = pd.Series(data)

model = ARIMA(series,order=(1,0,1))
model_fit = model.fit()

forecast = model_fit.forecast(steps=5)

print(f'predicition: {forecast}')

# Chi-Square Test
from scipy import stats

observed = [10,20,30]
expected = [15,15,30]

chi2_stat, p_value = stats.chisquare(f_obs=observed,f_exp=expected)
print(f'chi-Quadrat-Statisik:{chi2_stat},P:{p_value}')

# Survival Analysis
import numpy as np
from lifelines import KaplanMeierFitter

time = np.array([5,6,6,2,4,3])
event = np.array([1,1,1,0,1,0]) # 1 means happpend 0 means not happend

kmf = KaplanMeierFitter()

kmf.fit(time,event_observed=event)

kmf.plot_survival_function()