#09.10.2024

class Washer:
    height = 800
    width = 450
    def wash(self):
        print('I can wash clothes')

# wa = Washer()
# wa.wash()

class Person:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
    def play(self):
        print(f'{self.name} is gaming')
    def introduce(self):
        print(f'{self.name} is {self.age} years old and {self.height} cm')

pe = Person('Dagema',18,156)
#pe.play()
#pe.introduce()
# pe.age = 18
# pe.introduce()

# print(Person.name)

class ABC:
    def __init__(self):
        print("It is __init__(self) function")

# ABC()


class Renwu:
    def __init__(self):
        print('i am __init__(self)')
    def __del__(self):
        print('delete')
#n = Renwu()
#print('the last code')

# package
# 3 propoty : package, inherit, multi
# package: methode to hide some function or propoty

class Person:
    name = 'Alex'
pe = Person()
# print(pe.name)

# hide propoty
class Person:
    name = 'James'
    __age = 28
    def introduce(self):
        Person.__age = 3
        print(f'{Person.name} is {Person.__age} years old')
pe = Person()
# request hide propoty option 1
# print(pe._Person__age)
# request hide propoty option 2
# pe.introduce()

class Person:
    name = 'Thomas'
    __age = 54
    _sex = 'no info'

pe = Person()
# print(pe._sex)

class Man:
    def __play(self): # hide methode
        print('play handy')
    def funa(self):
        print('normal')
        # Man.__play(self) # Option 1
        self.__play()#

m = Man()
m.funa()

class Girl:
    def _buy(self):
        print('buy buy everyday')

g = Girl()
g._buy() 