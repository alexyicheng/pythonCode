# 16.11.2024

summe = 0
up = 2
down = 1
for i in range(20):
    summe += up/down
    a = down
    down = up
    up = up + a
print(summe)