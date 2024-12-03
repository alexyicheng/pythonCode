# 03.12.2024

__all__ = ['add'] # define from modulName import *
# which methode should be implemented


def add(a,b):
    print(a+b)

def output(a):
    print(a)

# to be sure that only methods used which define in testModul_1
if __name__ == '__main__':
    add(5,6)
    output(100)