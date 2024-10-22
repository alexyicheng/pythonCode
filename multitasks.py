# 20.10.2024

import time
import threading
from multiprocessing import Process, Queue
import os
# from queue import Queue

import form
from threading import Lock
from multiprocessing import process

from requests.packages import target


# def sing():
#     print('I am singing')
#     time.sleep(2) # sec
#     print('finished sing')
# def dance():
#     print('I am dancing')
#     time.sleep(2)
#     print('finished dance')
#
# sing()
# dance()

# multi tasks

# def sing(name):
#     print(f'{name} am singing')
#     time.sleep(2)
#     print('finished')
#
# def dance(name):
#     print(f'{name} am dancing')
#     time.sleep(2)
#     print('finished')
#
# # main programm entrance
# if __name__ == '__main__':
#     t1 = threading.Thread(target=sing,args=('Alex',)) # use tuple by only 1 element has to add , after element
#     # < Thread(Thread - 1(sing), initial) >
#     # print(t1)
#     t2 = threading.Thread(target=dance,args=('Alex',))
#     # setDaemon() has to create before start()
#     t1.daemon = True
#     t2.daemon = True
#     # stop main join(): break, has to define after start()
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print('Perfect finish, great show')

# def task():
#     time.sleep(2)
#     print('current:', threading.current_thread().name)
#
# if __name__ =='__main__':
#     for i in range(5):
#         t = threading.Thread(target=task)
#         t.start()

# sharing
# li = []
# def wdate():
#     for i in range(5):
#         li.append(i)
#         time.sleep(1)
#     print('inserting data:', li)
# def rdate():
#     print('reading data:',li)
#
# if __name__=='__main__':
#     wd = threading.Thread(target=wdate)
#     rd = threading.Thread(target=rdate)
#     wd.start()
#     wd.join()
#     rd.start()
#     rd.join()

# option 1
# a = 0
# b = 1000000
#
# def add():
#     for i in range(b):
#          global a
#          a += 1
#     print('first time:' ,a)
# def add2():
#     for i in range(b):
#          global a
#          a += 1
#     print('second time:', a)
#
# if __name__ == '__main__':
#     a1 = threading.Thread(target=add)
#     a2 = threading.Thread(target=add2)
#     a1.start()
#     a1.join() # wait first programm a1 finished, code runs second programm
#     a2.start()
#     a2.join()

# option 2
# lock = Lock()
#
# a = 0
# b = 1000000
#
# def add():
#     lock.acquire()
#     for i in range(b):
#          global a
#          a += 1
#     print('first time:' ,a)
#     lock.release()
# def add2():
#     lock.acquire()
#     for i in range(b):
#          global a
#          a += 1
#     print('second time:', a)
#     lock.release()
# if __name__ == '__main__':
#     a1 = threading.Thread(target=add)
#     a2 = threading.Thread(target=add2)
#     a1.start()
#     a2.start()


# multiprocessing

def sing():
    print(f'sing() sub programm pid:{os.getpid()}, main programm id: {os.getppid()}')
    print('singing')
def dance():
    print(f'dance() sub programm pid:{os.getpid()},main programm id: {os.getppid()}')
    print('Dancing')
# if __name__ == '__main__':
#     # create subprogramms
#     p1 = Process(target=sing,name='subprogramm1')
#     p2 = Process(target=dance,name='subprogramm2')
#     p1.start()
#     p2.start()
#     # change the name of subprogramms
#     p1.name='subprogramm_1'
#     p2.name='subprogramm_2'
#     print('p1:',p1.name)
#     print('p2:',p2.name)
#     print('p1.pid',p1.pid)
#     print('p2.pid',p2.pid)

def eat(name):
    print(f'{name} is eating')
def sleep(name):
    print(f'{name} is sleeping')
# if __name__ == '__main__':
#     p1 = Process(target=eat,args=('Alex',))
#     p2 = Process(target=sleep,args=('Sophia',))
#     p1.start()
#     p1.join()
#     p2.start()
#     print('p1 alive:', p1.is_alive())
#     print('p2 alive:', p2.is_alive())

li = []
def wdate():
    for i in range(5):
        li.append(i)
        time.sleep(1)
    print('inserting data:', li)
def rdate():
    print('reading data:',li)

# if __name__=='__main__':
#    p1 = Process(target=wdate)
#    p2 = Process(target=rdate)
#    p1.start()
#    p2.start()


# Queue
# q.put()
# q.get()
# q.empty()
# q.qsize()
# q.full()

q = Queue(3)
q.put('Money bank')
q.put('Dream comes be true')
q.put('Lol')
# print(q.qsize())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.empty())


li = ['Daniela','Alex','Sohpia','Elena']

def wdata(q1):
    for i in range(5):
        print(f'{i} is already inserted')
        q1.put(i)
        time.sleep(1)
    print('wirte data:',li)

def rdata(q2):
    while True:
        if q2.empty():
            break
        else:
            print('take element',q2.get())
    print('read date:',li)

# if __name__ == '__main__':
#     q = Queue()
#     p1 = Process(target=wdata,args=(q,))
#     p2 = Process(target=rdata,args=(q,))
#     p1.start()
#     p2.start()




