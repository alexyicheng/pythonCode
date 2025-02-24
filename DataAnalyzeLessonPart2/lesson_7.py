# 24.02.2025

def func():
    print('That is my first function')

# func()

def summe(list_1):
    count = 0
    for i in list_1:
        count += i
    print(count)

list_1 = {5,6,9,12,14}
# summe(list_1)

def get_sum(x,y):
    print(x+y)

# get_sum(2,3)
# get_sum(12,13)

def get_sum2(x=1,y=1):
    print(x+y)

# get_sum2(10,5)

def interview(name='Alex',age=33):
    print(f'Hallo alle Zusammen, ich bin {name} und {age} Jahre alt')

# interview('Dennis')

def get_diff(*x):
    print(x)

get_diff(1)
get_diff(1,2)
get_diff(1,5,9)

def get_diff2(*args,**kwargs):
    print(args) # empty
    print(kwargs)

get_diff2(a=1,y=2,c=5,d=10)
get_diff2() # empty