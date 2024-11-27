# 27.11.2024


"""
def functionname():
    function body
    return value
"""

def uselessfunction():
    result = 1+2
    return result
print(uselessfunction())

def get_sum(a,b):
    result = a + b
    return result
print(get_sum(5,9))

def proof_body_temperatur(body_celsius):
    if body_celsius <= 37.5:
        return 'normal, you are welcome'
    else:
        return 'Sorry, you are not able to go in'
result = proof_body_temperatur(37)
print(result)


# return multi values as result
def multireturnvalue():
    return 5,6,9

erg = multireturnvalue()
print(erg)
a,b,c = multireturnvalue()
print(f'first value of result(multireturnvalue) is {a}, second value of result(multireturnvalue) is {b}, third value of result(multireturnvalue) is {c}')

def newFunction():
    num = 10
    return num
print(newFunction())
# print(num) -> num exist only in the function newFunction()
# not able to use from outside

# gloabal Value
D = 81
def changeglobalvalueD():
    global D
    D = 100
    return D
changeglobalvalueD()
print(D)

# function into function
def f_b():
    print('function 2')

def f_a():
    print('function 1')
    f_b()
    print('function 3')

f_a()

def person_info(name,age,gender):
    print(f'name is {name}. {name} is {age} years old. {name} is {gender}.')

person_info('Alex',23,'man')
# use key word init the value -> without order of function Definition
person_info(age=18,name='Helena',gender='woman')

# default value in function
def user_info(name,gender,age=18):
    print(f'{name} is {gender}. The User is {age} years old')

user_info('Adas','man')
# default value could be overwritten -> new defined by insert the value
user_info('Nicole','woman',32)

# insert dynamic value of function
# type : tuple()
def employee_info(*args):
    print(args)
# depends on the condition of usage
employee_info('Daniela','is', 'pretty and intelligence')
employee_info() # define nothing

# dynamic key word value of function
# type : dictionary
def salary_info(**kwargs):
    print(kwargs)
salary_info(name='Alex',tax_class = 'I',basic_salary='8590.58€',project_bonus='5000€',employee_id=9255561)

# anonym value
def test_function(a):
    print(a)

def name():
    return 'ZhuiMengRen'

def plus(a,b):
    return a+b

test_function([1,2,3])
test_function(5)
test_function('Eileen')
test_function(name())
test_function(plus(1,8))

# Difference between normal and anonym function
# def key word, could define function with name
# lambda key word, could define anonym function
# function with name could repeat multitimes
# lambda function only 1 time
# lambda function
def threeValue(function):
    result = function(2,5,9)
    print(result)

def my_fun(a,b,c):
    return a+b+c

# threeValue(my_fun)
# same like threeValue(my_fun) without to create my_fun
threeValue(lambda a,b,c: a+b+c)
threeValue(lambda a,b,c: a*b*c)

# recursive function -> function that recall itself in itself
# output + recall itself
# 3+2+1
def sum_numbers(num):
    #ouput if num = 1 return 1
    if num == 1:
        return 1
    else:
        # recall itself sum_numbers(num-1)
        result = num + sum_numbers(num-1)
        return result
erg = sum_numbers(3)
print(erg)