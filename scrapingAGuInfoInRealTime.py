import akshare
import pandas
import matplotlib.pyplot as plt
# plt.figure(figsize=(18,10))

# get real time data
data = akshare.stock_zh_a_spot_em()
# print(data)

# get one share in the past
# his_data = akshare.stock_zh_a_hist(symbol='600519',period='daily',start_date='20150101',end_date='20231231')

# save history data as csv
# his_data.to_csv('GuiZhouMaoTai[600519]history.csv',index=False, encoding='utf-8')

# 5 Daily Average
df = pandas.read_csv('GuiZhouMaoTai[600519]history.csv',index_col=0,encoding='utf-8')

# D5 = df['收盘'].rolling(window=5).mean().plot(label='5 Daily')
# D10 = df['收盘'].rolling(window=10).mean().plot(label='10 Daily')
# D30 = df['收盘'].rolling(window=30).mean().plot(label='30 Daily')
# D60 = df['收盘'].rolling(window=60).mean().plot(label='60 Daily')

plt.rcParams['font.sans-serif']=['SimHei'] #Show Chinese label
plt.rcParams['axes.unicode_minus']=False   #These two lines need to be set manually

# plt.legend(loc='upper right', borderaxespad=0.)

df = df[['开盘','收盘','最高','最低','成交额']]
df_max_min = (df-df.min())/(df.max()-df.min())
df_max_min.plot(figsize=(15,8))
plt.show()