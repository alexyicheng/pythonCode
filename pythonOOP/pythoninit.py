# 04.12.2024

class Student(object):
    # name = None
    # age = None
    # address = None

    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.addr = address

    def output(self):
        print(self.name)
        print(self.age)
        print(self.addr)

# stu1 = Student()
# stu1.name = 'Alex'
# stu1.age = 18
# stu1.addr = 'British'

stu2 = Student('Helena',21,'German')
stu2.output()