# 26.02.2025
#
# def func():
#     print('function actived')
#
# print(func()) # None -> return nothing back
#
# def func2():
#     print('function actived')
#     return 1
#
# print(func2()) # 1 -> return 1
#
# def login(x,y):
#     if x=='Coco' and y == 123:
#         print('login successed')
#         return True
#     else:
#         return False
#
# def shoppingCart(x):
#     flag = login('Coco',578)
#     if flag:
#         print(f'User adds {x} into the shopping cart')
#     else:
#         print(f'login failed')
#
# shoppingCart('Dragenball Z')

# sum = 0
ls = [5,6,8]
print(sum(ls))

def func(a,b):
    c = a**2 + b
    b = a
    return c

a = 10
b= 100
c = func(a,b) + a
print(a,b,c)

for i in 'CHINA':
    for k in range(2):
        print(i, end = '')
        if i == 'N':
            break
