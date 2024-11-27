# 26.11.2024


# dict = {key:value,key:value,...}
book_list = {'Faust':50,'Die Zeit':30,'Lichtspiel':26,'Lichtspiel':32}
print(book_list)
# {'Faust': 50, 'Die Zeit': 30, 'Lichtspiel': 32}
# key should be unique, if 2 keys with same key the dictionary overwrite the key:value

# define empty dict
# option 1
dict1 = {}
print(type(dict1))
# option 2
my_dict = dict()
print(type(my_dict))

# add new value into dictionary
my_dict['Löwenherz'] = 26
print(my_dict)

# del element from dictionary
# option 1
del book_list['Lichtspiel']
# option 2
# del(book_list['Lichtspiel'])
print(book_list)

# empty the dictionary
my_dict.clear()
print(my_dict)
# empty dictionary = {}

# update element of dictionary
employee_dict = {'Daniela':18,'Alex':25,'Armin':50,'Julia':26}
employee_dict['Alex'] = 32
print(employee_dict)

# search element of dictionary
# option 1
print(f'Daniela is {employee_dict['Daniela']} years old')
# option 2
print('Armin is ' + str(employee_dict.get('Armin')) + ' years old')
# option 3 default value if the key doesnot exist in the dictionary
print(employee_dict.get('Helena',0))
# 0 -> 'Helena' doesnot exist in the employee_dict -> return the default value 0

# search all names of employee
employee_dict_name = employee_dict.keys()
print(employee_dict_name) # show all employee name
print(type(employee_dict_name)) # <class 'dict_keys'>
employee_dict_ages = employee_dict.values()
print(employee_dict_ages) # show all ages of everyone
employee_dict_items = employee_dict.items()
print(type(employee_dict_items)) # <class 'dict_items'>
print(employee_dict_items) # show everything of employee_dict

person_dict = {'name':'Helena','age':20,'gender':'w','living space':'Germany'}
# get all keys of dictionary
print(person_dict.keys())
for key in person_dict.keys():
    print(key)

# get all values of dictionary
print(person_dict.values())
for value in person_dict.values():
    print(value)

# get all elements of dictionary
print(person_dict.items())
for item in person_dict.items():
    print(item)
# option 2
for key,value in person_dict.items():
    print(key,':',value)




