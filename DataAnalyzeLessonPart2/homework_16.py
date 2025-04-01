import pandas as pd

data = pd.read_csv(r'C:\Users\AY\Desktop\pythonCode\DataAnalyzeLessonPart2\students_scores.csv')

df = pd.DataFrame(data)

df_withoutNaN = df.dropna()
# print(df_withoutNaN)

df_Filter = df_withoutNaN[df_withoutNaN['成绩']<=100]
# print(df_Filter)

df_drop_duplicates = df_Filter.drop_duplicates()
# print(df_drop_duplicates)  # Erstellt eine neue Kopie ohne Duplikate

# def func(x):
#     if x > 80:
#         return x

# new_df = df_drop_duplicates['成绩'].map(func)
# print(new_df)

new_df = df_drop_duplicates[df_drop_duplicates['成绩'] > 80]
print(new_df)
