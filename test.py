import random
def randomdef():
    listi = [2,4,6]
    return random.choice(listi)

class Nagdyr:

    def __init__(self,tegund,location,afl):
        self.location = location
        self.afl = afl
        self.tegund = tegund
    def prenta(self):
        print(self.tegund, self.afl, self.location)
    def newturn(self):
        self.location = random.randint ( 1, 100 )
        self.afl = randomdef ()

#rottur
rotta = Nagdyr("Rotta",location,afl)
rotta.prenta()
