#17.10.2024

#f = open(r'C:\Users\AY\Desktop\pythonCode\78!重生\第1章开局被女知青退婚.txt',encoding = "utf-8")
# option 1
# for i in f:
#     # print(f.readline())
#     # print(f.readlines())
#     print(i)
#option 2
# while True:
#     if not f.readline():
#         break
#     print(f.readline())
# f.close()

# create txt file
# file = open('test_1.txt','w')
# file.write('Hahaha That is my first txt file, create with python')
# file.close()

# add new element into txt file
# f = open('test_1.txt','a+')
# print(f.read())
# f.write('\ntest is being written')
# f.close()

# f = open('test.txt','w+')
# f.write('Hello Python')
# print(f.read())
#
# f.close()
# f = open('test.txt')
# print(f.read())
# f.close()

# tell() and seek()

# f = open('test.txt','w+') # w+ - first write after read
# f.write('hello Python')
# pos = f.tell()
# print(pos)
# pos2 = f.seek(0,0) # set up the pointer at the start again
# print(pos2)
# print(f.read()) # without f.seek(0,0) can not read the file because the pointer is behind 'hello Python'
# f.close()

# with open
# without use f.close()

# with open('test.txt','w') as f:
#     f.write('Hmmmm.....')

# with open('test.txt','w',encoding = 'utf-8') as f:
#     f.write('哈哈哈，小丑，歌德市最大的反派，扑克牌里最大的牌')

# with open('test.txt',encoding = 'utf-8') as f:
#     print(f.read())

import os
os.rename('test.txt','joke.txt')
os.remove() # delete
os.mkdir() # create new file
os.rmdir() # delete file
os.getcwd() # get current directory
os.listdir() # get current files of current directory


