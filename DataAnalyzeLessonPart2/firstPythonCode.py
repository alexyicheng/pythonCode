# 09.02.2025

a = (1,2,3,4,5,6,7,8,9,10)

print(a[9])

b = [4, 3, 5, 1, 2, 6]
print(b[1::2])

c = '上海自来水来自海上'
print(c.count('自'))
print(len(c))
print(c[0:2])
print(c[0::2])

names = []
names.append('张三')
names.append('李四')
names.append('王五')


names.insert(1,'赵六')
print(names)

names.pop(0)
names.insert(0,'zhangsan')
print(names)

names.insert(3,'孙七')
print(names)