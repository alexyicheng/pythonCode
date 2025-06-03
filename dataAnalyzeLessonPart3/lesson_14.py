# 29.05.2024

import numpy as np
import pandas as pd
import warnings
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler, PolynomialFeatures
warnings.filterwarnings('ignore')

df_train = pd.read_csv(r'C:\Users\AY\Desktop\数据集合\train.csv')
# print(df_train.head(5))
# print(df_train.shape)
# print(df_train.info())
# print(df_train.describe())
# print(df_train.duplicated().sum())
# print(df_train.isnull().mean())


arr = np.array([True,False,False,True,False,False,False,False,False,False])
# print(arr.mean())

# option1
# delete empty value dropna()
# insert empty value fillna()
# print(df_train['Age'].fillna(value=df_train['Age'].mean()))

# option2: sckit SimpleImputer
imp = SimpleImputer(strategy='mean')
df_train[['Age']] = imp.fit_transform(df_train[['Age']])
# df_train[['Age']] = imp.fit(df_train[['Age']].values)
# print(df_train.info())

df_train['Cabin'] = df_train['Cabin'].fillna(0)
# print(df_train['Cabin'].head(5))

# df_train['Embarked'].fillna(value=df_train['Embarked'].mode()[0])
df_train['Embarked'] = df_train['Embarked'].fillna(df_train['Embarked'].mode()[0])
# print(df_train['Embarked'])

# over visualization to know data distribution
# imp = SimpleImputer(strategy='mean')
# df_train[['Age']] = imp.fit_transform(df_train[['Age']])
#
# df_train['Cabin'] = df_train['Cabin'].fillna(0)
# df_train['Embarked'] = df_train['Embarked'].fillna(df_train['Embarked'].mode()[0])
fig,ax = plt.subplots(figsize=(12,4))
sns.kdeplot(df_train[df_train['Survived']==1]['Age'],label='Survived',shade=True,ax=ax)
sns.kdeplot(df_train[df_train['Survived']==0]['Age'],label='Not Survived',shade=True,ax=ax)
plt.legend()
ax.set_xlim(0,df_train['Age'].max())
# plt.show()

df_train['log_age']=df_train['Age'].apply(lambda x:np.log(x))
# print(df_train.head())

mm_scaler = MinMaxScaler()
fare_trans = mm_scaler.fit_transform(df_train[['Fare']])
# print(fare_trans)

std_scaler = StandardScaler()
fare_trans_std = std_scaler.fit_transform(df_train[['Fare']])
# print(fare_trans_std)

poly = PolynomialFeatures(degree=2)
# print(df_train[['SibSp','Parch']].head())

poly_fea = poly.fit_transform(df_train[['SibSp','Parch']])
# print(poly_fea)
# print(poly.get_feature_names_out(input_features=['SibSp','Parch']))

print(pd.get_dummies(df_train[['Embarked']]))
