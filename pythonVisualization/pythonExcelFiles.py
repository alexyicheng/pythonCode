# 05.12.2024

import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
from matplotlib import rcParams

# read csv file
data = pd.read_csv(r'C:\Users\AY\Desktop\数据集合\dataSet\Lesson_1\Example0.csv',encoding='GBK')
# rename columns
data.columns = ['names','values','insert_times']
# add chinese frontart
rcParams['font.family'] = 'SimSun'

# define the label,value and color
label = [ name for name in data['names']]
value = [value for value in data['values']]
color = ['#1f77b4','red','darkgreen','orange']

# define plot
fig,ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.15,right=0.83)
ax.set_title('Exam-Result')
ax.bar(label,value,label=label,color=color)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.legend()
plt.show()


