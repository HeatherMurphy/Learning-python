#Heather Murphy
#12/25/17
#sample class

class Flower(object):
    def __init__(self):
        self.color = 'Green'
        self.leaves = 1
class Daisy(Flower):
    def __init__(self):
        self.color = 'Yellow'
        self.leaves = 2

flowers = (['Daisy','Yellow',2],['Chrysanthemum','Red',3],['Orchid','Purple',6])
for flower in flowers: 
    class flower(Flower):
        def __init__(self):
            self.color = flower[1]
            self.leaves = flower[2]
   


flower1 = Daisy()
print (flower1.color, flower1.leaves, sep = '\n')

flower2 = Chrysanthemum()
print (flower2.color, flower2.leaves, sep = '\n')
                 
