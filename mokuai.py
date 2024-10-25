# 25.10.2024

import os
import sys
import time
import logging
import random

# name is property name() is methode
# print(os.name)
# Windows -> nt Linux -> posix

# print(os.getenv('path'))
# path of the py
# print(os.path.dirname(r'C:\Users\AY\Desktop\pythonCode\mokuai.py'))
# py file
# print(os.path.basename(r'C:\Users\AY\Desktop\pythonCode\mokuai.py'))

# exist the file or not
# print(os.path.exists(r'C:\Users\AY\Desktop\pythonCode\hellopython.py'))
# os.path.isfile()
# os.path.isdir()

# show the path of file
# print(os.path.abspath('mokuai.py'))
# print(os.path.isabs(r'C:\Users\AY\Desktop\pythonCode\mokuai.py'))


# print(sys.getdefaultencoding())
# print(sys.path)
#show the system
print(sys.platform)
# show the version of python
print(sys.version)

# get current time
print(time.time())

t1 = time.localtime()
# print(f'today is {t1.tm_year}-{t1.tm_mon}-{t1.tm_mday}')

t2 = time.asctime()
# print(t2)

# transform from float to day time typ
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

# transform from string to date time tuple
# print(time.strptime('2021-08-02','%Y-%m-%d'))

# CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
# define logging log.log file with format
# logging.basicConfig(filename='log.log',filemode='w',level=logging.NOTSET,format='%(levelname)s: %(asctime)s\t%(message)s')
# logging.debug('I am debug')
# logging.info('I am info')
# logging.warning('I am warning')
# logging.error('I am error')
# logging.critical('I am critical')
# logging level only over greater either warning

# always one float between 0 and 1 and never reach 1
print(random.random())

# create one float between a and b
print(random.uniform(1,3))

# create on integer between a and b
# print(random.randint(1,50))

print(random.randrange(5,100,10))

