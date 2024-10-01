#01.10.2024
# Funktion



def einlogen():
    print('bitte logen Sie ein.')
    username = input('Geben Sie bitte Ihren Benutzername ein:')
    passwort = input('Geben Sie bitte Ihr Passwort ein:')
    dict_1 = {'name':username,'pw':hash(passwort)}
    return dict_1

#print(einlogen())

# default value function
def einlogen(username='Empty',passwort='Empty'):
    dict_1 = {'name':username,'pw':hash(passwort)}
    return dict_1

#print(einlogen('Apple','Abc123'))
#print(einlogen())

# modifiable(changeable,editable) parameter in function
def funcA(*args):
    return (args)

# print(funcA('NY',2))

#key value function

def Alpha(**kwargs):
     return kwargs

#print(Alpha(name='Justin',age=30))

#function in function

def study():
    print('learning in the night')
    #function course() into function study()
    def course():
        print('basic of Python')
    course()

# study()

#globale Variable
# global a
# a = 'Hallo World'
# print(a)

#nonlocal Variable
#gilt nur für einen Level über
# a = 5
def outer():
    a = 10

    def inner():
        a = 20
        def inner2():
            nonlocal a  # #ndern den werte a von inner2() von 20 auf 30
            a = 30
            print('a von inner2()', a)
        inner2()
        print('a von inner()', a)
    inner()
    print('a von outer', a)
#outer()

# lambda funktion
# lambda braucht keinen Return Wert
add = lambda a,b : a+b
# print(add(5,4))

# abc = lambda name,age=18: (name, age)
# print(abc('Achim',30))

lambda_dict = lambda **kwargs:kwargs
#print(lambda_dict(name = 'Hans', alter = 56))

#lambda + if
comp = lambda a,b: 'a ist größer als b' if a > b else 'b ist größer als a'
#print(comp(5,8))

import builtins
#print(dir(builtins))
# Funktion start mit groß buchstaben

list_1 = [1,2,3]
# Alle Element um 5 erhöhen
aEu5e = lambda a: a+5
#map(funktion,item) funktion, item -  iterierbares Objekt
newErg = map(aEu5e,list_1)
#option 1
print(list(newErg))
#option 2
# for i in newErg:
#     print(i)

from functools import reduce
# reduce(function,sequence) - funktion , muss 2 variable besitzen, iterable
list_2 = [1,2,3,4]
def add_2(x,y):
    return x+2*y
# 1+2*2 = 5 -> 5+3*2 = 11 -> 11+4*2=19 -> return result 19
print(reduce(add_2,list_2))

# element einzelne aus der tupel entziehen
tua = (1,2,3,4,5)
a, *b = tua
print(a,b)
def tuaentnehmen(a,b,*args):
    print('a =',a)
    print('b =',b)
    print('args = ',args,type(args))
tuaentnehmen(a,b)

c,*d = b
print(c,d)





