# 04.12.2024

class Student(object):
    # object
    name = None # save name of student
    age = None
    address = None

    # method
    def say_hi(self):
        # self means:
        # keyword for member, have to defined
        # means itself
        print(f'introduce myself: My Name is {self.name}, i am {self.age} years old and live in {self.address}')
        return

    def study(self):
        print(f'{self.name} is learning')


# create object -> init student.name
student = Student()
# property
student.name = 'Alex'
student.age = 23
student.address = 'LA'
student.say_hi()
#
# student_2 = Student()
# student_2.name = 'Lana'
# student_2.age = 19
# student.address = 'Chicago'
# student_2.study()

class Smartphone(object):

    def __init__(self):
        self.IMEI = None
        self.producer = None
        self.__current_voltage = 33 # not necessary to show -> hide it

    def call_by_5G(self):
        print(f'5G is Calling...{self.__current_voltage}') # in method visit to over self.privateValue

    def __keep_single_core(self):
        print('Use CPU as Single Core to save energy')

# init Smartphone
smartphone = Smartphone()
smartphone.IMEI = 'APPLE001'
smartphone.producer = 'Apple'
# smartphone.__current_voltage = 33 # out of class -> not allow to use as privat value
# print(smartphone.__current_voltage) # no Error -> but useless
smartphone.call_by_5G()

