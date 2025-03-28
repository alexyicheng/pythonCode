'''
数组创建
使用 numpy 创建一个包含从0到9的数组。
创建一个全是3的形状为(2,3)的数组。


数组运算
创建一个10个元素的数组，值全为5，然后将其全部元素乘以3。
使用两个3x3的数组，计算它们的乘积。
数组1: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
数组2: [[9, 8, 7], [6, 5, 4], [3, 2, 1]]


索引和切片
创建一个包含从10到19的数组，提取其中的奇数元素。
创建一个4x4的二维数组，提取其中第三行和第四列。
创建一个4x4的二维数组，交换其中的第一列和第四列。
'''

import numpy as np

t1 = np.arange(0,10)
print(t1)

t2 = np.full((2,3),3)
print(t2)

t3 = np.full((2,5),5)
print(t3*3)

t4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
t5 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# 计算乘积 (矩阵乘法)
product = np.dot(t4,t5)
print(product)

t6 = np.arange(10,20)
new_t6 = t6[t6%2 != 0]
print(t6)
print(new_t6)

t7 = np.arange(1,17).reshape(4,4)
third_row = t7[2,:]
fourth_col = t7[:,3]
print(t7)
print(third_row)
print(fourth_col)

t7[:,[0,3]] = t7[:,[3,0]]
print(t7)