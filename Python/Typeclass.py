#Heather Murphy
#12/25/17
#TYPECLASSSSSSSS

class Stuff(object):
    def __init__(self):
        self.x = 5

Dragon = type('Dragon',(object,),{'x':12})

m = Stuff()
b = Dragon()

print (m.x, b.x, sep='\n')
