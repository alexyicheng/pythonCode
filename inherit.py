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

grandson = Grandson()
grandson.buy()
grandson.eat()

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

m = Man()
m.money()

