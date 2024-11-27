# 22.11.2024

# [start:end:step]
list_1 = [1,2,3,4,5,6,7,8,9]
new_list_1 = list_1[::2]
# [1, 3, 5, 7, 9]
print(new_list_1)
new_list_2 = list_1[:8:3]
# [1, 4, 7]
print(new_list_2)
new_list_3 = list_1[::-1]
# [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(new_list_3)