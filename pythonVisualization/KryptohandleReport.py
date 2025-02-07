# 19.12.2024
from itertools import groupby

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('TransactionExport.csv',encoding='utf-8',sep=';')
# count the rows in the file
# row_count = len(df)
# print(f'This Excel has {row_count} rows')

# all information about the single column -> for example ['TransactionType']
# print(df['TransactionType'].describe())

# check the dataFrameType of all columns
print(df.dtypes)

# # to show all columns
# pd.set_option('display.max_columns',None)
# # to show all name of columns and dataFrameType
# print(df.columns)

# print(df.head(5))

# which value are in the column TransactionType
# unique_values_TransactionType = df['TransactionType'].unique()
# print(unique_values_TransactionType)
# # how many actions are done
# TransactionType_counts = df['TransactionType'].value_counts()
# print(TransactionType_counts)
#
# # Which Currency are used to handle
# unique_values_Currency = df[' Currency'].unique()
# print(unique_values_Currency)
# Currency_counts = df[' Currency'].value_counts()
# print(Currency_counts)
#
# Which Kryptos are in handle
# unique_values_Asset = df[' Asset'].unique()
# print(unique_values_Asset)
# # How many times the crpyto is bought and sold
# Asset_counts = df[' Asset'].value_counts()
# print(Asset_counts)


# # Group by in pandas
# # the Sum of Buy,Sell,Deposit and Withdraw
# sum_TransactionTpye = df[['TransactionType',' EurAmount']].groupby('TransactionType').sum().sort_values(by=[' EurAmount'],ascending=True)
# print(sum_TransactionTpye)
# # the sum of sold and bought Krypto
# sum_Krypto = df[[' Asset','TransactionType',' EurAmount']].groupby([' Asset','TransactionType']).sum()
# print(sum_Krypto)

# select all Bitcoin Data of dataset
btc = df[df[' Asset'] == ' Btc']
btc_subset = btc[[' Asset','TransactionType',' Date',' EurAmount',' Currency']].groupby(['TransactionType',' Date']).sum().sort_values(by=['TransactionType',' Date'],ascending = False)

print(btc_subset)


