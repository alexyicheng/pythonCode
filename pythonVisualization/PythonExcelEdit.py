# 08.12.2024

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'SimSun'

# read Excel file
df = pd.read_excel(r'C:\Users\AY\Desktop\数据集合\dataSet\Lesson_2\thressStudent.xlsx')

students = [student for student in df['姓名']]
# print(students)

# show the values
print(df.head())

# show the type of values
print(df.dtypes)

# extract Exam of Chinese, Math, English
# 语文90 数学80 英语80
Exam_result = [result.split(' ') for result in df['考试结果'] ]

# [['语文90', '数学80', '英语80'], ['语文91', '数学50', '英语85'], ['语文54', '数学78', '英语66'], ['语文78', '数学63', '英语90']]
# Extract Value for result of Chinese Exam
Exam_result_Chinese = [result[0] for result in Exam_result]
Exam_result_Chinese_Value = [int(v[2:]) for v in Exam_result_Chinese]
print(f'Sum of Chinese Exam is {np.sum(Exam_result_Chinese_Value)}')
print(f'Average of Chinese Exam is {np.average(Exam_result_Chinese_Value)}')
print(f'Median of Math Chinese is {np.median(Exam_result_Chinese_Value)}')

# Extract Value for result of Math Exam
Exam_result_Math = [result[1] for result in Exam_result]
Exam_result_Math_Value = [int(v[2:]) for v in Exam_result_Math]
print(f'Sum of Math Exam is {np.sum(Exam_result_Math_Value)}')
print(f'Average of Math Exam is {np.average(Exam_result_Math_Value)}')
print(f'Median of Math Exam is {np.median(Exam_result_Math_Value)}')

# Extract Value for result of Englisch Exam
Exam_result_English = [result[2] for result in Exam_result]
Exam_result_English_Value = [int(v[2:]) for v in Exam_result_English]
print(f'Sum of English Exam is {np.sum(Exam_result_English_Value)}')
print(f'Average of English Exam is {np.average(Exam_result_English_Value)}')
print(f'Median of English Exam is {np.median(Exam_result_English_Value)}')

# create plots
# create plot for Chinese Exam
fig,axs = plt.subplots(1,3,figsize=(15,5))
value_0 = Exam_result_Chinese_Value
colors = ['red', 'blue', 'gold', 'orange']
axs[0].plot(students,Exam_result_Chinese_Value)
axs[0].set_title('Result of Chinese Exam')
axs[0].bar(students,value_0,label=value_0,color=colors)

# create plot for Math Exam
value_1 = Exam_result_Math_Value
colors = ['red', 'blue', 'gold', 'orange']
axs[1].plot(students,Exam_result_Math_Value)
axs[1].set_title('Result of Math Exam')
axs[1].bar(students,value_1,label=value_1,color=colors)

# create plot for English Exam
value_2 = Exam_result_English_Value
colors = ['red', 'blue', 'gold', 'orange']
axs[2].plot(students,Exam_result_English_Value)
axs[2].set_title('Result of English Exam')
axs[2].bar(students,value_2,label=value_2,color=colors)

for ax in axs:
    ax.legend()

plt.tight_layout() # optimize the graphic
plt.show()
