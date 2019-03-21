#Heather Murphy
#12/25/17
#decorator present

def Bow(Func):
    def addStuff(*args,**kwargs):
        return Func(*args,**kwargs) + ' ' + 'Bow'
    return addStuff
@Bow
def Present():
    return 'Pretty'
print (Present())
