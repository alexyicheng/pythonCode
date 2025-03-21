# 21.03.2025

import numpy as np

list_1 = [1,'1',1,[1,2]]
# print(list_1)
# [1, '1', 1, [1, 2]]
# numpy array only save the same data type
# print(np.array([4,5,'1']))
# ['4' '5' '1']

# b = np.arange(11) # 11 elements von 0 -10
# [ 0  1  2  3  4  5  6  7  8  9 10]
b = np.arange(1,11,2) # start von 1 to 11, step 2 elements pro step
# [1 3 5 7 9]
# print(b)

c = np.random.random(2) # create random floatnumber between 0-1
# print(c)

d = np.random.randint(5) # create random int between 0-5
e = np.random.randint(5,10) # create random int between 5-10
f = np.random.randint(5,10,5) # create 5 random int between 5-10
# print(f)

# g = np.zeros(10) # create 10 zero-elements in the array
g = np.zeros((2,3)) # 2 - rows, 3 - columns
# print(g)

h = np.ones(10) # create array with 10 element with 1
# print(h)

i = np.full((2,3),2)
# print(i)

np1 = np.arange(5)
# print(type(np1)) # check the np1 type
# print(np1.dtype) # check the element of array

np2 = np.array([1.1,2.2])
# print(np2.dtype)

np3 = np.array(['a','b'])
print(np3.dtype)

t1 = np.arange(10)
print(t1)
print(t1.shape)

t2 = np.array([[1,2],[3,4]])
print(t2)
print(t2.shape) # (2,2)

t3 = np.array([[1,2,3,4],[3,4,5,6]])
print(t3)
print(t3.shape) # (2,4)

# reshape the matrix
t4 = np.arange(1,13)
new_t4 = t4.reshape(3,4)
new_t4_1 = t4.reshape(1,2,6)
new_t4_2 = t4.reshape(2,2,3)
print(new_t4_2)