# 21.11.2024

# TUPEL
# index()
# count()
# len()
# del

t1 = ('sangenglaoshi',35,['Python Scraping','Data Scientist'])
# print(t1.index('sangenglaoshi'))
# print(len(t1))
del t1[2][0]
# print('new tuple list', t1)
t1[2].append('Python Djungo')
# print('after add Python Djungo element',t1)


# Strings
# find()
# index()
# count()
# len()
# replace()
# split()
# join()

str1 = 'hello World, hello Pyhton, hello China'
print(f'hello is {str1.rfind('hello')}')
print(len(str1))
print(f'hello is {str1.rindex('hello')}')
print(f'how many time are hello there, there are {str1.count('hello',0,38)} times')

new_str1 = str1.replace('hello','hi')
print(new_str1)
list1 = str1.split(',')
print(list1)
new_list1 = ' |'.join(list1)
print(new_list1)