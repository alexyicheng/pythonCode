# 28.11.2024


# 1. create interface to show the options
# 2. insert request
# 3. depends on which user request are -> aktion
# define function
# use function

# 1. create interface
# define function to show the system opportunity

def show_options():
    print('-'*40)
    print('Welcome to the Student Controlling System!')
    print('1. Insert new student')
    print('2. Delete student')
    print('3. Update student info')
    print('4. Research student info')
    print('5. Show all info of students')
    print('6. Quit')
    print('-'*40)

# define the memory of student info
student_info = []

# insert student info
# 1. get and save student_info
# 2. check, ob the student already existed in the system
# 2.1 if the student already existed -> show error
# 2.2 if the student donot exist in the system
#     -> create empty dictionary -> add info into dictionary
# 3. implemt by correct space

def add_student_info():
    global student_info
    print('please insert follow info -> StudentID, name, and mobile')
    new_id = int(input('please insert your student ID: '))
    new_name = input('please insert your name: ')
    new_tel = input('please insert your mobile: ')
    # proof if the student already existed
    for student in student_info:
        if new_name == student['name']:
            print('student existed already')
            return
    # after checking new student -> insert it into student_info

    # define dictionary to save the student_info
    # option 1
    student_dict = {'ID':new_id,'name':new_name,'mobile':new_tel}
    # option 2
    # student_dict = {}
    # student_dict['ID'] = new_id
    # student_dict['name'] = new_name
    # student_dict['mobile'] = new_tel
    student_info.append(student_dict)

    print(student_info)

# rearticulate student
# 1. insert student ID
# 2. proof if the student existed already or not
# 2.1 if existed -> rearticulate
# 2.2 if not -> show error and new input
# 3. use on correct place
def rearticulate_student_info():
    global student_info
    while True:
        del_id = int(input('please your student ID'))
        # option 1
        for student in student_info:
            if del_id == student['ID']:
                f = input('Do you really want to rearticulate this student? y or n')
                if f.upper() == 'Y':
                    student_info.remove(student)
                print(student_info)
            else:
                print('student doesnot exist, rewrote it, please')
        # option 2 donot work anymore python change it
        # if 0 <= del_id < len(student_info):
        #     f = input('Do you really want to rearticulate this student? y or n')
        #     if f.upper() == 'Y':
        #         del student_info[del_id]
        #         print(student_info)
        # print('student doesnot exist, rewrote it, please')

# update/modify sutdent_info
# 1. user insert goal student ID
# 2. proof if the student existed
# 2.1 if existed -> show the info of student -> update student info
# 2.2 if not -> show error -> new insert
# 3. use on correct space
def update_student_info():
    global student_info
    while True:
        student_ID = int(input('please insert your student ID'))
        for student in student_info:
            if student_ID == student['ID']:
                print(f'student_ID: {student['ID']}\n'
                      f'student_name: {student['name']}\n'
                      f'student_mobile:{student['mobile']}')
                # student ID should be unique unchangable

                new_name = input('insert new name: ')
                new_tel = input('insert new mobile: ')

                # collect new details for the user
                updates = {}
                if new_name:
                    updates['name'] = new_name
                if new_tel:
                    updates['mobile'] = new_tel

                # update the student info
                student.update(updates)

                print('update success')
                print(student_info)
                return
            else:
                print('Error: Student_ID doesnot existed')
                continue
        # option 2
        # """Updates a student's information."""
        # global student_info
        # upd_id = int(input('Enter the Student ID to update: '))
        #
        # for student in student_info:
        #     if upd_id == student['ID']:
        #         print(f'Current info: {student}')
        #         student['Name'] = input('Enter new Name: ') or student['Name']
        #         student['Mobile'] = input('Enter new Mobile Number: ') or student['Mobile']
        #         print('Student updated successfully.')
        #         print(student)
        #         return
        #
        # print('Error: Student ID not found.')

def search_student_info():
    while True:
        user_ID =int(input('please insert your student_id to check your infomartion'))
        for student in student_info:
            if user_ID == student['ID']:
                print(student)
                return
            else:
                print('please proof your insert student_ID')
                print('There are not in the system')
                continue

def show_all_student_info():
    global student_info
    if not student_info:
        print('There are no student Info there')
        return
    else:
        print('All Students:')
        for student in student_info:
            print(student)
            # return # there to insert return is wrong -> it stops the iteration
            # show only 1 student not all -> for this reason delete it

while True:
    show_options()
    # 2. insert request
    # catch the error insert by string
    try:
        user_input = int(input('please insert the number of option: '))
    except ValueError:
        print('Error: Please insert a valid number.')
        continue

    if user_input == 1:
        add_student_info()
    elif user_input == 2:
        rearticulate_student_info()
    elif user_input == 3:
        update_student_info()
    elif user_input == 4:
        search_student_info()
    elif user_input == 5:
        show_all_student_info()
    elif user_input == 6:
        print('Quit')
        break # quit system
    else:
        print('undefined Option, Error')
