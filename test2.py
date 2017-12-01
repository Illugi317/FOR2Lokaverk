import random
import time
#Illugi og Eyþór

class Nagdyr:
    def __init__(self,location,afl,tegund):
        self.location = location
        self.afl = afl
        self.tegund = tegund
    def musnewturn(self):
        kast = random.randint(1,6)
        self.location += kast
        if self.location > 100:
            self.location = 100
        return str(kast)
    def rottanewturn(self):
        listi = [1,2]
        choice = random.choice(listi)
        if choice == 1:
            self.location += random.randint(1,6)
        elif choice == 2:
            self.location -= random.randint(1,6)

        if self.location > 100:
            self.location = 100
        elif self.location < 0:
            self.location = 0
    def hamsturnewturn(self,mus):
        if self.location > mus.location:
            print("Hamstur fer afturábak til músar sem er á reit",mus.location,"og hamstur er á",self.location)
            self.location -= random.randint(1,6)
        elif self.location < mus.location:
            print("Hamstur fer áfram til músar sem er á reit",mus.location,"og hamstur er á",self.location)
            self.location += random.randint(1,6)



def baratta(mus,rotta):
    print("Mús þarf að berjast við rottu")
    if mus.afl > rotta.afl:
        print("MÚS VANN LETS GO +2 LOC")
        mus.location += 2
    elif mus.afl == rotta.afl:
        print("Jafntefli 0+- loc")
        mus.location += 0
    elif rotta.afl > mus.afl:
        print("Mús er weak shit -2 loc")
        mus.location -= 2

def hamstrahelp(mus,hamstur):
    print("Hamstur ætlar sér að hjálpa músar fellanum")
    mus.location += hamstur.afl
    hamstur.location += int(hamstur.afl/2)
    print("Hamstur færir mús um",hamstur.afl,"reiti")
    print("Hamstur færist einnig um",int(hamstur.afl/2),"reiti")
    print("Mús er á reit",mus.location)

def hamsturogrotta(hamstur,rotta):
    print("Rotta og hamstur rákust á! þeir hrökklast frá hvorum öðrum.")
    rotta.location -=1
    hamstur.location+=1
    print("Hamstur er nú á reit",hamstur.location)
    print("Rotta er nú á reit",rotta.location)

def happareitur(mus):
    happa=random.randint(1,2)
    if happa==1:
        print("Mikið er þessi mús óheppin! 10 reiti til baka!")
        mus.location -= 10
    elif happa==2:
        print("Heppin mús! 10 reiti áfram!")
        mus.location += 10

def randomafl():
    listi = [2,4,6]
    return random.choice(listi)
def main():
    mus = Nagdyr(1,randomafl(),"Mús")
    kost=0
    rotta1 = Nagdyr(random.randint(0,100),randomafl(),"Rotta")
    rotta2 = Nagdyr(random.randint(0,100),randomafl(),"Rotta")
    rotta3 = Nagdyr(random.randint(0,100),randomafl(),"Rotta")
    hamstur = Nagdyr(random.randint(0,100),randomafl(),"Hamstur")
    time.sleep(0.5)
    while True:
        if mus.location >= 100:
            print("jei musin vann shi mar, þetta tók ekki nema",kost,"köst!")
            break
        old1 = rotta1.location
        old2 = rotta2.location
        old3 = rotta3.location
        old4 = mus.location
        old5 = hamstur.location
        rotta1.rottanewturn ()
        rotta2.rottanewturn ()
        rotta3.rottanewturn ()
        hamstur.hamsturnewturn(mus)
        print("Mús er á reit :", mus.location)
        print("Rotta 1 er á reit :", rotta1.location)
        print("Rotta 2 er á reit :", rotta2.location)
        print("Rotta 3 er á reit :", rotta3.location)
        print("Hamstur er á reit :", hamstur.location)
        kost=kost+1
        print("Mus færðist um "+mus.musnewturn()+" reiti")
        if old4 < old1:
            if mus.location >= rotta1.location:
                baratta(mus,rotta1)
        if old4 < old2:
            if mus.location >= rotta2.location:
                baratta ( mus, rotta2 )
        if old4 < old3:
            if mus.location >= rotta3.location:
                baratta ( mus, rotta3 )
        if old4 < old5:
            if mus.location >= hamstur.location:
                hamstrahelp(mus, hamstur)
        if old5 == old1:
            hamsturogrotta(hamstur,rotta1)
        if old5 == old2:
            hamsturogrotta(hamstur,rotta2)
        if old5 == old3:
            hamsturogrotta(hamstur,rotta3)
        if mus.location == 50:
            happareitur(mus)
        print(old4,old5)
        time.sleep(0.5)
main()
