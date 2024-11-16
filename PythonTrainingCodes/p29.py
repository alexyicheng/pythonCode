# 16.11.2024

import math

# methode_1
n = 4
sum = 1
for i in range(1,n+1):
    sum *= i
print(sum)

# methode_2
def falcultät(num):
    if num == 1:
        return 1
    else:
        return num * falcultät(num-1)
print(falcultät(5))

# methode_3
sum_3 = 0
for i in range(1,21):
    sum_3 += math.factorial(i)
print(sum_3)