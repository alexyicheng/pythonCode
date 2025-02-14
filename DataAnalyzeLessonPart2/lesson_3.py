# 14.02.2025

s = 'abcdef'

# a b c d e f
# 0 1 2 3 4 5
# -6-5-4-3-2-1
# for string in s:
#     print(string)

print(s[2]) # c
print(s[0:2]) # ab
print(s[1:4]) # bcd

# string[start:end:step]
print(s[0:5:2]) # ace

print(s[:2:]) # ab
print(s[2::]) # cdef

s_2 = 'a,b,c,d'
print(s_2[::2]) # abcd
print(s_2.split(','))

price = '100.5Mio-200.5Mio'
print(price.split('-'))

# s_3 = 'hello'
# print(s_3.upper())
# print(s_3.lower())

# code = 'Ab2C'
# code_input = input(f'Bitte geben sie Sicherheitscode ein')
# print(code.lower()==code_input.lower())
# print(code.upper()==code_input.upper())

s_4 = 'Ich lerne Python, es macht Spaß. Spaß macht Python'
# print(s_4.replace('Python','C++'))
# print(len(s_4))
# print(s_4.count('spaß'))

l_1 = ['Daniela','Eileen','Aelx','Wolfgang']
print(l_1[1])
print(l_1[-1])
print(l_1[0:2])
print(l_1[1:4])
print(l_1[0:4:2])
print(l_1[:])
print(len(l_1))
print(l_1.append('Jürgen')) # None -> only for append without print
l_1.append('Uwe')
print(l_1)

# l_1.insert(index,)
l_1.insert(3,'Fredrick')
print(l_1)

# update
l_1[1] = 'Jessica'
print(l_1)

print(l_1.pop()) # delete element -> return delete element
l_1.pop() # automatic delete last element of list
print(l_1)

l_1.pop(3) # delete index = 3 element of list
print(l_1)

l_1.remove('Aelx')
print(l_1)

# proof if Element Daniela in the list
print('Daniela'in l_1) # True

l_2 = [11,88,55,33,66,99,100]
print(max(l_2))
print(min(l_2))
print(sum(l_2))
print(sorted(l_2)) # from small to great
print(sorted(l_2,reverse=True)) # reverse

l_3 = [1,2,[11,22,33]]
print(len(l_3))
print(l_3[2][:])

l_3.append(44)
print(l_3)

l_3[2].append(55)
print(l_3)