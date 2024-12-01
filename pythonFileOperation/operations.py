# 01.12.2024

# File Operations:
# open
# read
# close

# open(name,mode,encoding)
# name : file path + filename
# mode : which operation do your want to use: read, write, add
# r read file
# w write file
# a add file
# encoding: CodeModus(perf UTF-8)

# f = open(f'DemoCode.txt',mode='r',encoding='utf-8')

# read
# read() read everything
# read(num) read specified byte
# readlines() get list array
# readline() get only 1 line

# line = f.readline()
# while line:
#     print(line)
#     line = f.readline()
#
# # close()
# f.close()

with open('DemoCode.txt','r',encoding='utf-8') as f:
    # option 1
    # for line in f:
    #     print(line)
    # option 2
    text = f.read()
    print(text)

# write text into file
with open('DemoCode.txt','w',encoding='utf-8') as f:
    f.write('JB Lifestyler\n')
    f.write('hahaha, joker -> Please come back, batmans say he will never hit you again.')
    f.flush()

print('successed')

# add
# if file doesonot exist -> create it
with open('DemoCode.txt','a') as f:
    f.write('Lol, your noise is falling, dude\n')
    f.flush()