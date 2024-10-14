# 08.10.2024

# recall itself without using other function

# fibonacci zahlen
# 1,1,2,3,5,8,13,...

def fibo(a):
    if a <= 1:
        return a
    return fibo(a-2)+fibo(a-1)

#print(fibo(5))

def outer(m):
    n = 10
    def inner():
        print('n+m=',m+n)
    return inner # only the name of function not inner() otherwise return error message
#recall the function Option 1
#outer()()

#recall the function Option 2
# os = outer(5)
# os()

# interface
# without change code, add new function

# option 1
# def send():
#     print('Nachrichten senden')
#
# def send2():
#     print('überweisung 520')
#
# def outer2(fn):
#     def inner2():
#         print('Login')
#         fn()
#     return inner2
# print(outer2(send))
# outer2(send2)()


#option 2
# def outer3(fn):
#     def inner3():
#         print('login')
#         fn()
#     return inner3
# @outer3
# def send3():
#     print('hahaha')
# send3()
# @outer3
# def send4():
#     print('Nachrichten hallo')
# send4()

# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# def waibao(fn):
#     def neibao(*args, **kwargs):
#         print('Login')
#         fn(*args,**kwargs)
#     return neibao
# ot = waibao(func)
# ot('susu','tangtang',name = 'Gerhard',age=80)

# several interface

def interface1(fn):
    def inner():
        return 'Hahaha'+fn()+'LoL'
    return inner

def interface2(fn):
    def inner():
        return 'nice'+fn()+'Oh yeah'
    return inner
@interface1
@interface2
def test():
    return 'learn python'

print(test())

