# 04.12.2024

# magic Candy means
# python automatic implement methods
# use for special method like __init__(self), __str__(self) and so on

class Student(object):
    def __init__(self,name,age,addr):
        self.name = name
        self.age = age
        self.addr = addr

    def __str__(self):
        return f'name is {self.name}, age is {self.age}, address is {self.addr}'

    def __eq__(self,other):
        if self.age == other.age:
            print('same age')
        else:
            print('not same age')


stu_1 = Student('Alex',21,'Holland')
# without __str__(self)
print(stu_1) # <__main__.Student object at 0x00000228CEABB380>
# with __str__(self)
# name is Alex, age is 21, address is Holland

stu_2 = Student('Alex',23,'German')
# print(stu_1 == stu_2) # compare place of storage
# without __eq__(self) False
stu_1.__eq__(stu_2)

