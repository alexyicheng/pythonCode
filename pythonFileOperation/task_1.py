# 01.12.2024

count = 0
with open('DemoCode.txt','r',encoding='utf-8') as f:
    for line in f:
        c = line.count('World')
        count += c
print(f'World are {count} times in the file')