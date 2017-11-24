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
        print("Rotta er á reit",self.location)
    def newturn(self):
        kast = random.randint ( -6, 6 )
        self.location += kast
        if self.location > 100:
            self.location = 100
        elif self.location < 0:
            self.location = 0
    def locationreturn(self):
        return self.location

'''
        if self.location < 1:
            self.location += random.randint(1,6)
        elif self.location < 0:
            self.location = 0
        elif self.location > 100:
            self.location = 100
        else:
            self.location += random.randint(-6,6)
'''

class Mus:
    def __init__(self,location,afl):
        self.location = location
        self.afl = afl
    def newturn(self):
        self.location += random.randint(1,6)
    def prenta(self):
        if self.location > 100:
            self.location = 100
        print("Mús er á reit",self.location)
    def locationreturn(self):
        return self.location

def baratta(musobj,rottaobj):
    print("Mús þarf að berjast við rottu")
    if musobj.afl > rottaobj.afl:
        musobj.location += 2
    elif musobj.afl == rottaobj.afl:
        musobj.location += 0
    else:
        musobj.location -= 2
def hvorrotta(mus,rotta1,rotta2,rotta3,listi):
        for x in range(listi):
            if x == rotta1:
                return rotta1
            elif x == rotta2:
                return rotta2
            elif x == rotta3:
                return rotta3
            else:
                pass

def main():
    mus = Mus(1,randomdef())
    rotta1 = Nagdyr("Rotta",random.randint(1,100),randomdef())
    rotta2 = Nagdyr("Rotta",random.randint(1,100),randomdef())
    rotta3 = Nagdyr("Rotta",random.randint(1,100),randomdef())
    while mus.location < 100:
        listi = []
        oldmus = mus.locationreturn ()
        mus.newturn ()
        rotta1.newturn()
        rotta2.newturn()
        rotta3.newturn()
        rotta1.prenta()
        rotta2.prenta()
        rotta3.prenta()
        mus.prenta()
        for x in range(oldmus,mus.locationreturn()):
            listi.append(x)
        if len(listi) == 1:
            pass
        else:
            try:
                listi.pop(0)
            except (IndexError):
                pass
             
        print("Kastar",len(listi),listi)
        hvorrotta(mus,rotta1,rotta2,rotta3,listi)

main()