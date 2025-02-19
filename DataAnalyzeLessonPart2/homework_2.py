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

papier = 2
stone = 1
scissors = 0

input_PC = random.randint(0,2)
while True:
    input_human = int(input('please insert papier,stone or scissors'))
    if input_PC == input_human:
        print('correct')
        break
    elif input_PC > input_human:
        print('to small')
    else:
        print('to big')



