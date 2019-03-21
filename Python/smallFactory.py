#Heather Murphy
#12/25/17
#factories...
BaseClass = type('BaseClass', (object,),{})

@classmethod
def Check1(self, myStr):
    return myStr == 'ham'
@classmethod
def Check2(self, myStr):
    return myStr == 'sandwich'
@classmethod
def Check3 (self, myStr):
    return myStr == 'meowmix'

C1 = type('C1',(BaseClass,),{'x':1, 'Check':Check1})
C2 = type('C2',(BaseClass,),{'x':30, 'Check':Check2})
C3 = type('C3',(BaseClass,),{'x':1200, 'Check':Check3})

def MyFactory(myStr):
    for cls in BaseClass.__subclasses__():
        if cls.Check(myStr):
            return cls

m = MyFactory('ham')
v = MyFactory('sandwich')
c = MyFactory('meowmix')
print (m.x, v.x, c.x, sep = '\n')
