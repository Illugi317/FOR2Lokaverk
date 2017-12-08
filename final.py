import random
import time
#Illugi og Eyþór

class Nagdyr:
    def __init__(self,location,afl,weight,tegund): #Smiðurinn tekur inn location,afl,þyngd og tegund
        self.location = location
        self.afl = afl
        self.tegund = tegund
        self.weight = weight
    def musnewturn(self):  # Þetta er class object function fyrir músina
        kast = random.randint(1,6) #Hvað er kastið mikið
        self.location += kast #bæta kastinu við locationið hjá músinni
        if self.location > 100: #ef kastið er meira en 100 þá skráir functonið það sem 100
            self.location = 100
        return str(kast) #til að sjá hversu marga reiti músinn fer
    def rottanewturn(self): #hérna er class object function fyrir rottuna
        listi = [1,2] #listi
        choice = random.choice(listi) #Til að velja hvort rottan fer áfram eða afturábak
        if choice == 1:
            self.location += random.randint(1,6) #áfram um X
        elif choice == 2:
            self.location -= random.randint(1,6) #tilbaka um X

        if self.location > 100:
            self.location = 100   #Leiðrétta ef rottan fer yfir spilar reitana
        elif self.location < 0:
            self.location = 0
    def hamsturnewturn(self,mus):#Class Objcet Function fyrir hamsturinn
        if self.location > mus.location: #Til að elta músinna afturábak
            print("Hamstur fer afturábak til músar sem er á reit",mus.location,"og hamstur er á",self.location)
            self.location -= random.randint(1,6) #random kast til að fara áfram
        elif self.location < mus.location:#Til að elta músinna áfram
            print("Hamstur fer áfram til músar sem er á reit",mus.location,"og hamstur er á",self.location)
            self.location += random.randint(1,6) #random kast til að fara afturábak
def baratta(mus,rotta): #Function sem tekur inn mus object og rottu object til að láta berjast
    print("Mús þarf að BERJAST við rottu")
    if mus.afl > rotta.afl and mus.weight == 750 and rotta.weight == 250:
        print("MÚS VANN LETS GO +2 LOC")
        mus.location += 2
    elif rotta.afl > mus.afl and mus.weight == 750 and rotta.weight == 250:
        print("Mús vann vegna þyngdar")
        mus.location += 2
    elif mus.afl == rotta.afl and mus.weight == 750 and rotta.weight == 250: #Hér eru 7 if setingar til að finna út hver vinnur og hvort músinn fer áfram
        print("Mús vann vegna þyngdar --")
        mus.location +=2
    elif mus.afl == rotta.afl and mus.weight == 500 or rotta.afl == 500:
        print("Jafntefli!")
        mus.location += 0
    elif mus.afl == rotta.afl and mus.weight == 250 and rotta.weight == 750:
        print("Rotta vann vegna þyngdar++")
        mus.location -= 2
    elif rotta.afl > mus.afl and mus.weight == 250 and rotta.weight == 750:
        print("Mús er weak shit -2 loc//")
        mus.location -= 2
    elif rotta.afl > mus.afl and mus.weight == 500 or rotta.weight == 500:
        print("Rottan er sterkari, mus er weak shit -2 loc")
        mus.location -= 2

def hamstrahelp(mus,hamstur): #Function sem tekur inn hamstur obj og músar obj
    print("Hamstur ætlar sér að hjálpa músar fellanum")
    mus.location += hamstur.afl #Hjálpa músinni um hversu mikið afl hamsturinn er með
    hamstur.location += int(hamstur.afl/2) # Hamsturinn fer helmings afls sitt áfram
    print("Hamstur færir mús um",hamstur.afl,"reiti")
    print("Hamstur færist einnig um",int(hamstur.afl/2),"reiti") #Prenta út hversu langt mus og hamstur fór fyrir notanda
    print("Mús er á reit",mus.location)

def hamsturogrotta(hamstur,rotta): #Function sem tekur inn hamstur og rottu obj
    print("Rotta og hamstur rákust á! þeir hrökklast frá hvorum öðrum.")
    rotta.location -=1   #Hér er bara látirð rottuna fara afturábak um 1 og hamstur áfram um 1
    hamstur.location+=1
    print("Hamstur er nú á reit",hamstur.location) #prenta út fyrir notanda
    print("Rotta er nú á reit",rotta.location)

def happareitur(mus): #Function fyrir happa reitinn
    happa=random.randint(1,2) #Til að velja hvort músinn fer áfram um 5 eða tilbaka um 5
    if happa==1:
        print("Mikið er þessi mús óheppin! 5 reiti til baka!")
        mus.location -= 5
    elif happa==2:
        print("Heppin mús! 5 reiti áfram!")
        mus.location += 5

def weight(): #Function fyrir til að returna þyngd
    listi = [250,500,750]
    return random.choice(listi)

def randomafl():#Function til að returna þyngd
    listi = [2,4,6]
    return random.choice(listi)

def main(): #Main function sem main forritið byrjar í og endar í (frekar c based)
    mus = Nagdyr(1,randomafl(),weight(),"Mús") #Búa til mus class object
    kost=0 #Hversu mörg köst það tekur til vinna handa músinni basically teljari
    rotta1 = Nagdyr(random.randint(0,100),randomafl(),weight(),"Rotta")
    rotta2 = Nagdyr(random.randint(0,100),randomafl(),weight(),"Rotta") #Búa til rottu objectinn og hamsturinn
    rotta3 = Nagdyr(random.randint(0,100),randomafl(),weight(),"Rotta")
    hamstur = Nagdyr(random.randint(0,100),randomafl(),weight(),"Hamstur")
    print("Mús er með :",mus.afl) #Prenta út hversu mikið afl músinn er með og hversu þung hún er
    print("Mús er með :",mus.weight)
    print("rotta1 :",rotta1.weight)
    print("Rotta2 :",rotta2.weight) #Þyngd og afl hjá rottum
    print("Rotta3 :",rotta3.weight)
    print("rotta1 afl:",rotta1.afl)
    print("rotta2 afl:",rotta2.afl)
    print("rotta3 afl:",rotta3.afl)
    time.sleep(1)
    while True: #While lykkja fyrir aðal leikinn
        if mus.location >= 100: #Ef músinn er kominn á  þennan reit skal prenta hversu oft hún þurfti að kasta og breakar while lykkjuna
            print("jei musin vann shi mar, þetta tók ekki nema",kost,"köst!")
            break
        old1 = rotta1.location
        old2 = rotta2.location #oldX til að geyma gömlu locationinn til að geta trackað hvort músinn rekst við rottur
        old3 = rotta3.location #eða hvort hamstur rekst við rottur
        old4 = mus.location
        old5 = hamstur.location
        rotta1.rottanewturn ()
        rotta2.rottanewturn ()
        rotta3.rottanewturn ()
        hamstur.hamsturnewturn(mus)
        print("Mús er á reit :", mus.location)
        print("Rotta 1 er á reit :", rotta1.location) #prenta út staðsetningu hjá mús og rottum og hamstri
        print("Rotta 2 er á reit :", rotta2.location)
        print("Rotta 3 er á reit :", rotta3.location)
        print("Hamstur er á reit :", hamstur.location)
        kost=kost+1 #Bæta við kastar teljaran
        print("Mus færðist um "+mus.musnewturn()+" reiti")
        if old4 < old1:
            if mus.location >= rotta1.location:
                baratta(mus,rotta1)
        if old4 < old2:
            if mus.location >= rotta2.location:
                baratta (mus,rotta2)          #Þessar if setningar eru til að tracka hvort músinn rekst við rottur
        if old4 < old3:
            if mus.location >= rotta3.location:
                baratta (mus,rotta3)
        if old4 < old5:  #Þessi er ef mús og hamstur hittast þá triggerast hamstrahelp()
            if mus.location >= hamstur.location:
                hamstrahelp(mus, hamstur)
        if hamstur.location == rotta1.location:
            hamsturogrotta(hamstur,rotta1)
        if hamstur.location == rotta2.location: #Hér er aðalega bara ef hamstur og rotta eru á sama reit
            hamsturogrotta(hamstur,rotta2)
        if hamstur.location == rotta3.location:
            hamsturogrotta(hamstur,rotta3)
        if mus.location == 50: #Happareitur fyrir músinna
            happareitur(mus)
main()
