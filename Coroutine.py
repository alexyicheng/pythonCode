# 22.10.2024

from greenlet import greenlet
import gevent
import time
from gevent import monkey

def task1():
    yield 'a'
    yield 'hahaha'
def task2():
    yield 'b'
    yield 'lol'

# if __name__ == '__main__':
#     t1 = task1()
#     t2 = task2()
    # print(next(t1))
    # print(next(t1))
    # print(next(t2))
    # print(next(t2))
    # for i in range(2):
    #     print(next(t1))
    #     print(next(t2))

def sing():
    print('Singing')
    # time.sleep(5)
    gevent.sleep(5)
    print('finished sing')
def dance():
    print('dancing')
    # time.sleep(3)
    gevent.sleep(3)
    print('finished dance')

# if __name__ == '__main__':
#     g1 = greenlet(sing)
#     g2 = greenlet(dance)
#     g1.switch()
#     g2.switch()

# gevent: by I/O command -> automatic toggle
# gevent.spawn()
# gevent.sleep()
# gevent.joinall()

# if __name__ == '__main__':
#     g1 = gevent.spawn(sing)
#     g2 = gevent.spawn(dance)
#     g1.join() # wait til  g1 finished
#     g2.join()

# def speak(name):
#     for i in range(3):
#         gevent.sleep(1) # processing in the same time
#         # time.sleep(1) # processing one by one
#         print(f'{name} is speacking now, and {i} time')
#
# if __name__ == '__main__':
#     gevent.joinall([
#         gevent.spawn(speak,'Daniela'),
#         gevent.spawn(speak, 'Alex')
#     ])

# monkey patch
monkey.patch_all() # time.sleep() = gevent.sleep() -> processing in the same time
# important to know has to be before the patch
def speak(name):
    for i in range(3):
        time.sleep(1) # processing one by one
        print(f'{name} is speacking now, and {i} time')

if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(speak,'Daniela'),
        gevent.spawn(speak, 'Alex')
    ])


