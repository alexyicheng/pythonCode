# 12.12.2024

import pandas as pd
import numpy as np

# import excel file
data = pd.read_excel(r'C:\Users\AY\Desktop\数据集合\dataSet\Lesson_2\Exam_4.xlsx')
# define data
df = pd.DataFrame(data)
# rename column names
df.columns = ['Name','Chinese','Math','English']
print(df.head())

# find missing values of math exam
bool_series = pd.isnull(df['Math'])
missing_math_exam = df[bool_series]
print(missing_math_exam)

# find no missing values of math exam
bool_series = pd.notnull(df['Math'])
math_exam = df[bool_series]
print(math_exam)

