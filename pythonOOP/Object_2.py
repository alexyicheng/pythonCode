# 15.10.2024



class Person(object):
    name = 'Sophia'
    def __init__(self):
        self.age = 18
    def play(self):
        # print(f'{self.name} plays game') # Option 1
        print(f'{Person.name} plays game') # Option 2
        print(self.age)
    @staticmethod
    def introduce():
        print(f'I am {Person.name}')
    @classmethod
    def vorstellen(cls):
        print(cls.name)

# pe = Person()
# pe.play()
# pe.introduce()
# pe.vorstellen()

class Test(object):
    def __init__(self):
        print('It is __init__()')
    def __new__(cls, *args, **kwargs):
        print('__new__()')
        # expand father class methode
        res = super().__new__(cls)  #rewrite methode
        return res
        # import : overwrite __new__() have to use return super().__new__(cls) otherwise python doesnot have memory
# te = Test()

class Person(object):
    def __new__(cls, *args, **kwargs):
        print('it is __new__()')
        return super().__new__(cls)
    def __init__(self,name):
        self.name = name
        print('Name is',name)
# pe = Person('Alex')

# Summary
# __new__() create object
# __init__() init object

class Singleton(object):
    obj = None
    def __new__(cls, *args, **kwargs):
        print('That is __new__() function')
        #if cls.obj is empty
        if cls.obj == None:
            cls.obj = super().__new__(cls)
        return cls.obj
    def __init__(self):
        print('This is __init__()')

# s = Singleton()
# print('s:',s)
# s2 = Singleton()
# print('s2:',s2)


