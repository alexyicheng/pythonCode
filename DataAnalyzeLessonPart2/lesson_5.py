# 19.02.2025

import random

a = 50

if a < 100:
    print('a ist kleiner als 100')

num= random.randint(1,100)
# print(num)
# num_input = input('bitte geben sie eine Zahl ein')
# if num == int(num_input):
#     print('korrekt')
# else:
#     print('Falsch geraten')


# num_input = int(input('bitte geben sie eine Zahl ein'))
# if num < num_input:
#     print('zu groß')
# elif num > num_input:
#     print('zu klein')
# else:
#     print('richtig geraten')

# s = 45
# 80-100: Ausgezeichnet
#71-80: Befriedigend
# 60-70: Ausreichend
# kleiner 60: Mangelhaft

# if s > 80:
#     print('Ausgezeichnet')
# elif s >= 71 and s < 80:
#     print('Befriedigend')
# elif s > 59 and s <= 70:
#     print('Ausreichend')
# else:
#     print('Mangelhaft')
#
# a = 0
# while a < 5:
#     print(a)
#     a += 1

# count = 0
# result = random.randint(1,100)
# print(result)
# while count < 5:
#     number = int(input('Bitte geben sie eine Zahl ein'))
#     if result < number:
#         print('zu groß')
#     elif result > number:
#         print('zu klein')
#     else:
#         print('korrekt')
#         break
#     count += 1

# username = 'admin'
# password = 'admin123'
# input_count = 0
# while input_count < 3:
#     username_input = input('Bitte geben sie Ihr Username ein')
#     password_input = input('Bitte geben sie Ihr Password ein')
#     if username == username_input and password == password_input:
#         print('erfolgreich eingeloggt')
#         break
#     else:
#         print('Fehl geschlagen')
#     input_count += 1

# username = 'admin'
# password = 'admin123'
# while True:
#     username_input = input('Bitte geben sie Ihr Username ein')
#     password_input = input('Bitte geben sie Ihr Password ein')
#     if username == username_input and password == password_input:
#         print('erfolgreich eingeloggt')
#         break
#     else:
#         print('Fehl geschlagen')

# all odd number from 1 to 100
# a = 1
# while a <= 100:
#     if a % 2 == 0:
#         print(a)
#     a += 1

# a = 0
# sum = 0
# ls = [52,85,96,34,123]
# while a < len(ls):
#     sum = sum + ls[a]
#     a += 1
# print(sum)

s = 'variable ist gleich index'
index = 0
while index < len(s):
    print(s[index])
    index += 1

tuple_1 = (1,2,3,5,6)
index = 0
while index < len(tuple_1):
    print(tuple_1[index])
    index += 1