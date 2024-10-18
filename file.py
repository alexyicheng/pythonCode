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
f = open('test_1.txt','a+')
print(f.read())
f.write('\ntest is being written')
f.close()