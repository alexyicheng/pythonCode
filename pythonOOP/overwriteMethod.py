# 04.12.2024

class HandySystem(object):
    def system(self):
        print('That is my Handy System')

class IOS(HandySystem):
    # overwrite system() from class HandySystem()
    def system(self):
        print('Apple uses IOS System')

Handy = IOS()
# overwrite the system() method of HandySystem()
# use own method system
Handy.system()