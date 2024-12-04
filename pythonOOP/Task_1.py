# 04.12.2024

# option 1
# class Student(object):
#     name = None
#     age = None
#     address = None
#
#     def ausgabe(self):
#         print(f'Name:{self.name}')
#         print(f'Age:{self.age}')
#         print(f'Address:{self.address}')
#
# stu = Student()
# for i in range(2):
#     if i == 0:
#         name = input('please insert your name: ')
#         stu.name = name
#     elif i == 1:
#         age = int(input('please insert your age: '))
#         stu.age = age
#     elif i == 2:
#         address = input('please insert your address: ')
#         stu.address = address
#
# stu.ausgabe()

# option 2
class Student:

    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

# define a list to save the information of student
student_list = []

for i in range(10):
    print(f'please insert number{i+1} information of student')
    # prompt insert student data
    name = input('please insert your name')
    age = input('please insert your age')
    address = input('please insert your address')
    # init Student()
    stu = Student(name,age,address)
    # output student information
    print(f'student{i+1} insert successed. name: {stu.name} age: {stu.age} address: {stu.address}')
    # add into student_List
    student_list.append(stu)
