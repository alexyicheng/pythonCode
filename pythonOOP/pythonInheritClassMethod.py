# 04.12.2024

# inherit in life
# Smartphone: Apple, Samsung, Google, Xiaomi, Huawei
# Data Management: Data Analyst, Data Engine, Data Science

class Animal(object):
    def __init__(self):
        self.name = None
        self.race = None

    def say_hi(self):
        print(f'{self.name} is saying, Hi')

class Human(object):
    def __init__(self,human_name,human_age):
        self.human_name = 'Pethaver'
        self.human_age = 25

    def buy_food(self):
        print(f'{self.human_name} is buying food for his pet')

# inherit the property from Animal() and Human()
# priosation of Class -> (from left to right)
class Poodle(Animal,Human):
    def __init__(self):
        # own property of Poodle()
        self.property = 'almost happy'

    def fuck(self):
        print(f'{self.name} is fucking everywhere. Crazy Poodle')

# Test
# init class Poodle()
Hacky = Poodle()
Hacky.name = 'Hacky'
Hacky.race = 'Poodle'
# Poodle() own method
Hacky.fuck()
# Poodle() own property
print(Hacky.property)
# inherit say_hi() method and use it
Hacky.say_hi()
# inherit human_name from class Human()
# init human_name of class Human()
Hacky.human_name = 'Hongying'
# inherit Human() method
Hacky.buy_food()



