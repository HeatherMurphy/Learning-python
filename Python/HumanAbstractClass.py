#Heather Murphy
#12/25/17
#Human abstract class

from abc import ABCMeta, abstractmethod

class Human(object):
    __metaclass__=ABCMeta
    @abstractmethod
    def run (self):
        pass
    
class Robot(object):
    __metaclass__=ABCMeta
    @abstractmethod
    def vacuum (self, enemy):
        pass

class Cyborg(Human,Robot):
        def __init__(self):
            super(Cyborg,self).__init__()
        def Laserbeam(self, enemy):
            return enemy.health-20
Cyborg = Cyborg()
