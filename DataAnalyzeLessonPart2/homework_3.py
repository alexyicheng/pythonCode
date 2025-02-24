# 21.02.2025

students = [
   {'name' : '张三', 'age' : 23, 'score' : 88, 'tel' : '23423532', 'gender' : '男'},
   {'name' : '李四', 'age' : 26, 'score' : 80, 'tel' : '12533453', 'gender' : '女'},
   {'name' : '王五', 'age' : 15, 'score' : 58, 'tel' : '56453453', 'gender' : '男'},
   {'name' : '赵六', 'age' : 16, 'score' : 57, 'tel' : '86786785', 'gender' : '不明'},
   {'name' : '小明', 'age' : 18, 'score' : 98, 'tel' : '23434656', 'gender' : '女'},
   {'name' : '小红', 'age' : 23, 'score' : 72, 'tel' : '67867868', 'gender' : '女'}
]

count = 0
for student in students:
    if student['score'] <= 60:
        print(f'name:{student['name']}, score:{student['score']}')
        count += 1
print(f'There are {count} students, failed the exam')

students_scores = {
   "张三": {"语文": 90, "数学": 85, "英语": 88},
   "李四": {"语文": 92, "数学": 80, "英语": 86},
   "王五": {"语文": 85, "数学": 78, "英语": 90}
}

for key,value in students_scores.items():
    summe = 0
    for k,v in  value.items():
        summe = summe + v
    print(f'{key} average is {round(summe/len(value),2)}')

for key,value in students_scores.items():
    avg_score = sum(value.values())/len(value)
    print(f'{key}的平均成绩是{round(avg_score,2)}')

fruits = ["苹果", "香蕉", "苹果", "橘子", "香蕉", "苹果"]
fruit_count = {}
for fruit in fruits:
    fruit_count[fruit] = fruit_count.get(fruit,0) + 1
print(fruit_count)

from collections import Counter
fruit_count = dict(Counter(fruits))
print(fruit_count)

fruits_set = set(fruits)
ls_dict = {}
for fruit in fruits_set:
    ls_dict[fruit] = fruits.count(fruit)
print(ls_dict)

