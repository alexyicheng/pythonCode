def maximum(a=1,b=0):
    if a > b:
        print(a)
    elif a < b:
        print(b)
    else:
        print('a und b is same')

maximum()

def firstandlastalphabet(s):
    if not s:
        print('empty')
    else:
        print(f'first alphabet is {s[0]} and last alphabet is {s[-1]}')

firstandlastalphabet('Hello Python')
