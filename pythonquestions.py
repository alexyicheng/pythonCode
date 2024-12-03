# 25.10.2024
import math

erg = []
for i in range(2000,3200):
    if (i%7==0) and (i%5!=0):
        erg.append(i)
    i += 1
# print(erg)

def fact(x):
    if x==0:
        return 1
    else:
        return x * fact(x-1)
# x = int(input('insert the number to calculate the factorial:'))
# print(fact(x))

dic = {}
for i in range(1,9):
    dic[i]=i*i # append() does not work because append() is update element not add new element
    i += 1
# print(dic)

# li = []
# for i in range(1,5):
#     li.append(input(f'Please insert {i}.element'))
# print(f'this is list:,{li},this is tuple {tuple(li)}')

class InOutString(object):
    def __init__(self):
        self.s = ''
    def getstring(self):
        print('Please insert text:')
        self.s = input()
    def printstring(self):
        print(self.s.upper())

# if __name__ == '__main__':
#     strObj = InOutString()
#     strObj.getstring()
#     strObj.printstring()

c = 50
h = 30
value = []
# print('pleaes insert some number:')
# items = [x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
#     print(','.join(value))

my_list = [1,2,3].remove(3)
print(my_list)

my_string = 'ABCDEFGHIJ'
print(my_string[::-1])
print(my_string[1:5]) # BCDE




