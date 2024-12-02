# 02.12.2024

# try:
#     # print(num) # num -> not defined
#     print(1/0) # ZeroDivision not allowed
# except (NameError,ZeroDivisionError) as e:
#     print(e)

# finally -> Error or not Error -> close file
# try:
#     f = open('a.text','r',encoding='utf-8') # a.text not existed
# except:
#     f = open('b.text','w',encoding='utf-8') # catch error a.text not there -> create b.text
# else:
#     print('no Error')
# finally: # whatever Error or not -> close file
#     f.close()

# error handover
def f1():
    print('f1 starts ...')
    print(1/0) # ZeroDivision
    print('f1 ends ...')

def f2():
    print('f2 starts ...')
    try: # catch Error of f1()
        f1()
    except Exception as e:
        print(f'Error in f2: {e}')
    print('f2 ends ...')

def main():
    try: # catch
        f2()
    except Exception as e:
        print(e)

main()