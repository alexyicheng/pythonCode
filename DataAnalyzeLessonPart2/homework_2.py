# 19.02.2025

import random

# input_1 = int(input('please insert one number to prof modulo 2 and 5 in same time '))
# if input_1 % 2 == 0 and input_1 % 5 == 0:
#     print('possible')
# else:
#     print('not possible')

# sum_2 = 0
# i = 0
# while i <= 100:
#     if i % 7 != 0:
#         sum_2 = sum_2 + i
#         i += 1
#     else:
#         i += 1
# print(sum_2)


stone = 0
scissors = 1
papier = 2

info = {0:'stone',1:'scissors',2:'papier'}
while True:
    input_PC = random.randint(0,2)
    input_human = int(input('please insert papier,stone or scissors'))
    if input_human == -1:
        break
    if input_human in [0,1,2]:
        if input_PC == input_human:
            print(f'PC wählt {info[input_PC]},human wählt {info[input_human]},gleich stand')
        elif (input_PC == 0 and input_human == 1) or (input_PC == 1 and input_human == 2) or (input_PC == 2 and input_human == 0):
            print(f'PC wählt {info[input_PC]},human wählt {info[input_human]},PC hat gewonnen')
        else:
            f'PC wählt {info[input_PC]},human wählt {info[input_human]},Mensch hat gewonnen'
    else:
        print('please insert stone,scissors and paper')





