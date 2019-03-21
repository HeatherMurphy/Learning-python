#Heather Murphy
#12/27/17
#cat FSM

from random import randint
from time import clock

state = type('state',(object,),{})

class walk(state):
    def execute(self):
        print('Walking...')

class meow(state):
    def execute(self):
        print("'Meow!!'")
        
class meow(state):
    def execute(self):
        print("'Meow!!'")

class sleep(state):
    def execute(self):
        print("'ZZZZZZZZZZZ......'")
############################################################
class transition(object):
    def __init__(self, toState):
        self.toState = toState

def Execute(self):
    print('Transitioning...')

############################################################

class simpleFSM(object):
    def __init__(self,char):
        self.char = char
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.trans = None
    def setState(self, stateName):
        self.curState = self.states[stateName]
    def transition (self, transName):
        self.trans = self.transitions[transName]
        self.execute()
    def execute(self):
        if (self.trans):
            self.setState(self.trans.toState)
            self.trans = None
        self.curState.execute()    

#############################################################

class Char(object):
    def __init__(self):
        self.FSM = simpleFSM(self)
        self.sleep = True
        self.walk = False
        self.meow = False

###############################################################

if __name__ == '__main__':
    cat = Char()
    cat.FSM.states['sleep'] = sleep()
    cat.FSM.states['meow'] = meow()
    cat.FSM.states['walk'] = walk()
    cat.FSM.transitions['toSleep'] = transition('sleep')
    cat.FSM.transitions['toMeow'] = transition('meow')
    cat.FSM.transitions['toWalk'] = transition('walk')

    cat.FSM.setState('sleep')

    for i in range(10):
        startTime = clock()
        timeInterval = 1
        while (startTime + timeInterval >clock()):
            pass
        if (randint(0,2)):
            if (cat.sleep):
                cat.FSM.transition('toMeow')
                cat.sleep = False
                cat.walk = False
                cat.meow = True
            elif (cat.meow):
                cat.FSM.transition('toWalk')
                cat.meow = False
                cat.walk = True
                cat.sleep = False
        else:
            cat.FSM.transition('toSleep')
            cat.sleep = True
            cat.walk = False
            cat.meow = False

        cat.FSM.execute()
          
