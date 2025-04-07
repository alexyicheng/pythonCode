# 02.04.2024

import pandas as pd
import numpy as np

dates = ['2025-01-01','2025-02-01','2025-03-01']

print(pd.to_datetime(dates))

pd.date_range(start='2025-01-01',end = '2024-04-02',freq='W')

t = pd.Timestamp('2025-04-02 19:45:20')
# print(t.year)
# print(t.month)
# print(t.day)
# print(t.hour)
# print(t.minute)
# print(t.second)

dates = pd.date_range(start='2025-01-01',periods=5)
df = pd.DataFrame({'date':dates})
df['new_date'] = df['date']+pd.Timedelta(days=5)
print(df)

dates_1 = pd.date_range(start='2025-01-01',periods=5)
df = pd.DataFrame({'value':np.random.random(len(dates_1))},index=dates_1)
print(df)
data = df.reset_index()
print(data)
data.columns = ['Date','Value']
print(data)
data['year']=data['Date'].dt.year
data['month']=data['Date'].dt.month
data['day']=data['Date'].dt.day
print(data)

