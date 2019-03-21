#Heather Murphy
#12/25/17
#args and kwargs

def Meowmix(*args,**kwargs):
    for arg in args:
        print(arg)
    #make sure to put .items() method so it prints the contents of
    #the variable
    for arg in kwargs.items():
        print (arg)


Meowmix(25, g=26)
