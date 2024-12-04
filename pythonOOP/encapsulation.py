# 04.12.2024

# create class Phone()
class Phone(object):
    # define init object
    def __init__(self):
        self.__is_5G_enable = False
    # privat method
    def __check_5g(self):
        if self.__is_5G_enable:
            print('5G enable')
        else:
            print('5G off, use 4G')
    # public method
    def call_by_5G(self):
        # use privat method
        self.__check_5g()
        print('calling')

# test
p1 = Phone()
p1.call_by_5G()
