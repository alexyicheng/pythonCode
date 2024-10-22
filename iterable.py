# 19.10.2024

# Types: str,list,tuple,dict,set
# __iter__()
# __next__()
# isinstance()

from collections.abc import Iterable, Iterator

st = '123'
# isinstance(o,t) o = object, t = type
# print(isinstance(st,Iterable))
# print(isinstance(st,str))
# print(isinstance(st,(int,dict)))


# for i in st:
#     print(i)

li = [1,2,3,4,5]
# for i in li:
#     print(i)

# iter(),next()
# li2 = iter(li) # option 1
# print(li2)
# <list_iterator object at 0x000001E919685B40> = Iterator
# print(next(li2))
# print(next(li2))
# print(next(li2))
# print(next(li2))
# print(next(li2))
# # after take all elements, still use next() will receive error StopIteration
# print(next(li2))


# option 2
# li2 = li.__iter__()
# print(li2.__next__())
# print(li2.__next__())
# print(li2.__next__())
# print(li2.__next__())
# print(li2.__next__())
# print(li2.__next__())

# Iterable object -  Iterator

# name = 'PangMao'
# print(isinstance(name,Iterable))
# print(isinstance(name,Iterator))
# # with iter() change Iterable object to Iterator
# new_name = iter(name)
# print(isinstance(new_name,Iterable))
# print(isinstance(new_name,Iterator))

# dir() show the methode and object

# class Test(object):
#     def __init__(self):
#         self.num = 1
#     def funca(self):
#         print(self.num)
#         self.num += 1
# test = Test()
# print(test)
# for i in range(5):
#     test.funca()

class MyIterator:
    def __init__(self):
        self.num = 0
    def __iter__(self):
        return self # return current Iterator itself
    def __next__(self):
        if self.num == 5:
            raise StopIteration('Stop Iteration, no Elements anymore')
        self.num += 1
        return self.num

# mi = MyIterator()
# print(mi)
# print(mi.__next__())
# print(next(mi))

# for i in mi:
#     print(i)

# Generator
# for i in range(5):
#     print(i*5)

li2 = [i*5 for i in range(5)]
# print(li2)
# use () -> <generator object <genexpr> at 0x00000281FE8FA190>
gen = (i*5 for i in range(5))
# print(gen)
# get the elements of generator
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# # Error : StopIterator
# print(next(gen))

# Generator function - yield
# yield is like return
# yield stop function and save the iteration of the function

li3 = []
def test():
    li3 = []
    li3.append('a')
    li3.append('c')
    print('li3:', li3)
# test()

def gen(n):
    li4 = []
    li4.append(n)
    print('start')
    yield 'a'
    yield 'b'
    yield 'c'
# <generator object gen at 0x000002B26CE8D6C0>
# print(gen())
# gen_1 = gen()
# print(next(gen_1))
# print(next(gen_1))
# print(next(gen_1))
# # Error Stop Iteration
# print(next(gen_1))

def gen2(n):
    li = []
    # option 1
    # for i in range(n):
    #     li.append(i)
    # option 2
    a = 0
    while a < n:
        # li.append(a)
        yield a # option 3
        a += 1
    print('li: ', li)

gen2(4)

# for i in gen2(4):
# print(i)

def  Test():
    yield 1
    yield 2
    yield 3

ta = Test()
print(next(ta)) # use object
print(next(ta))
print(next(ta))
print(next(Test())) # use function without object
print(next(Test()))

