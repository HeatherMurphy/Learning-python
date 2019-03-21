#Heather Murphy
#12/25/17
#metaclass... i hope

def singleton(type):
    _instances = {}
    def __call__(cls, *args,**kwargs):
        #how does m.x not exist...
        if cls not in cls._instances:
            #what does __call__ do??
            cls._instances[cls]= super(singleton,cls).__call__(*args,**kwargs)
            cls.y = 5
            cls.x = 0
            cls.z = 1200
        return cls._instances[cls]

class MyClass(object):
    #metaclass must be like a decorator... passing MyClass through
    #the singleton function
    __metaclass__ = singleton

m = MyClass()
v = MyClass()
print (m.z)
m.x = 10
print (v.z)


            
        
