#Heather Murphy
#12/25/17
#decorators

def sandwichPlus(Func):
    def addOne(*args, **kwargs):
        return Func(*args,**kwargs)+ 'Sandwich'
    return addOne
@sandwichPlus
def printHam():
    return 'Ham'


print (printHam())
