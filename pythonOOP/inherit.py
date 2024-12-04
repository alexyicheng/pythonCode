# 14.10.2024

class Person:
    def eat(self):
        print('I can eating')
    def sing(self):
        print('I can singing')

class Girl(Person):
    pass

class Boy(Person):
    None

# girl = Girl()
# girl.eat()
# girl.sing()
# boy = Boy()
# boy.eat()
# boy.sing()

class Father:
    def eat(self):
        print('eating food')
    def sleep(self):
        print('sleeping')

class Son(Father):
    def buy(self):
        print('money money money')
    pass

class Grandson(Son):
    pass

# grandson = Grandson()
# grandson.buy()
# grandson.eat()

class Person:
    def money(self):
        print('1 Million Euro')
class Man(Person):
    def money(self):
        print('I earn 10 Million Euro')
        #inherit the methode of father class
        #option 1
        # Person.money(self)
        #option 2 best One
        super().money()
        #option 3
        # super(Man,self).money()

# m = Man()
# m.money()

#inherit multi father classes
class Father(object):
    def money(self):
        print('100 Million')
class Mother(object):
    def money(self):
        print('120 Million')
    def appearance(self):
        print('most beautiful')
class Son(Mother,Father):
    def money(self):
        print('100 thousand')
    pass


# by multi father class has the same function -> use the closer father class
# Son().money()
# Son().appearance()
# print(Son.__mro__)

class Animal(object):
    #father class : Animal
    def shout(self):
        print('Animal can shout')
    def eat(self):
        print('I can eat')
class Cat(Animal):
    #son class:cat
    def shout(self):
        print('Miao Miao Miao')
class Dog(Animal):
    #son class2:dog
    def shout(self):
        print('Wang Wang Wang')
    def eat(self):
        print('Dog eats dog food')
class Pig(Animal):
    def eat(self):
        print('Pig eats pig food')

# cat = Cat()
# cat.shout()
# dog = Dog()
# dog.shout()


def test(obj):
    obj.eat()

# animal = Animal()
# test(animal)
# pig = Pig()
# test(pig)

#static methode
# @staticmethode without using self,cls variable

class Person(object):
    @staticmethod
    def study(self):
        print(f'{self} can learn')

# Person.study('Alex')
# pe = Person()
# pe.study('Armin')

class Person(object):
    name = 'Thomas'
    @classmethod
    def sleep(cls):
        print(cls)
        print('Human sleeps')
        print(cls.name)
Person.sleep()
