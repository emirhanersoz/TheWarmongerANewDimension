class Faction:
    
    __doc__= "Faction Class"
    
    def __init__(self, name, numberUnits, attackPoint, healthPoint, unitRegenerationNumber):
        
        self.name = name
        self.numberUnits = numberUnits
        self.attackPoint = attackPoint
        self.healthPoint = healthPoint
        self.unitRegenerationNumber = unitRegenerationNumber
        
        self.totalHealth = numberUnits * healthPoint
        self.isAlive = True
        
        self.receiveAttack = 0
        self.gold = 0
        
    def AssgnEnemies(self):
        print(self.isAlive)
        return
    
    def PerformAttack(self, FactionI, FactionII):
        return
    
    def ReceiveAttack(self, receiveAttack, Faction):
        return
    
    def PurchaseWeapons(self):
        return
    
    def PurchaseArmors(self):
        return
    
    def Print(self):
        
        print('Faction Name:' , self.name)
        
        if self.isAlive == True:
            print('Status:', 'Alive')
            
        elif self.isAlive == False:
            print('Status:', 'Defeated')
        
        else:
            print('Status:', 'Warning')
            
        print('Number of Units:', self.numberUnits)
        print('Attack Point:', self.attackPoint)
        print('Health Point:', self.healthPoint)
        print('Unit Regen Number:', self.unitRegenerationNumber)
        print('Total Faction Health:' , self.totalHealth)
        print('\n')
        
    def EndTurn(self):
        
        if self.numberUnits <= 0:
            self.numberUnits = 0
            self.isAlive = False
            
        self.totalHealth = self.numberUnits * self.healthPoint 
        


class Merchant():
    
    __doc__= "Merchant Class"
    
    def __init__(self, startingWeaponPoint, startingArmorPoint, revenue, 
                 weaponPoint,armorPoint):
    
        self.startingWeaponPoint = startingWeaponPoint
        self.startingArmorPoint = startingArmorPoint
        self.revenue = 0
        self.weaponPoint = weaponPoint
        self.armorPoint = armorPoint
    
    def AssgnFactions():
        return
    
    def SellWeapons(self):
        return True

    def SellArmors():
        return
    
    def EndTurn():
        return
    
    
    
firstFaction = Merchant(10, 10, 360, 5, 6)           #Orcs
secondFaction = Merchant(12, 12, 300, 8, 9)          #Dwarves
thirtFaction = Merchant(8, 8, 400, 7, 6)             #Elves



OrcsArmy = Faction("Faction_I",55,35,130,11)         #Orcs
DwarvesArmy = Faction("Faction_II",50,30,150,10)     #Dwarves
ElvesArmy = Faction("Faction_III",60,25,125,12)      #Elves



class Orcs(Faction):
    
    __doc__= "Orcs Class"
    
    firstEnemy = DwarvesArmy        #Dwarves
    secondEnemy = ElvesArmy         #Elves 
    
    def __init__(self):
        pass
    
    def PerformAttack(self, factionI, factionII):
        
       if Orcs.firstEnemy.isAlive == True and Orcs.secondEnemy.isAlive == True:
           Orcs.firstEnemy.receiveAttack = ((OrcsArmy.numberUnits * 30)/100) * OrcsArmy.attackPoint
           Orcs.secondEnemy.receiveAttack = ((OrcsArmy.numberUnits * 70)/100) * OrcsArmy.attackPoint
           
           factionI.ReceiveAttack(Orcs.firstEnemy.receiveAttack, Orcs)
           factionII.ReceiveAttack(Orcs.secondEnemy.receiveAttack, Orcs)
           
           return print("İki Düşman Hayatta")
       
       elif Orcs.firstEnemy.isAlive == True and Orcs.secondEnemy.isAlive == False:
           Orcs.firstEnemy.receiveAttack = OrcsArmy.numberUnits * OrcsArmy.attackPoint 
           factionI.ReceiveAttack(Orcs.firstEnemy.receiveAttack, Orcs)
           return print("Bir Düşman da Öldü")
       
       elif Orcs.firstEnemy.isAlive == False and Orcs.secondEnemy.isAlive == True:
           Orcs.secondEnemy.receiveAttack = OrcsArmy.numberUnits * OrcsArmy.attackPoint 
           factionII.ReceiveAttack(Orcs.secondEnemy.receiveAttack, Orcs)
           return print("Bir Düşman Hayatta") 
    
       else:
           return print("İki Düşman da Ölü")
     
    def ReceiveAttack(self, receiveAttack, faction):
        
        if faction == Dwarves:
            receiveAttack = (receiveAttack * 80) / 100
        
        elif faction == Elves:
            receiveAttack = (receiveAttack * 75) / 100
        
        else:
            print("Saldırı Yok")
      
        Orcs.numberUnits -= receiveAttack / Orcs.healthPoint 
        return print("Orcs Saldırı Aldı")
    
    def Print(self):  
        print("“Stop running, you’ll only die tired!”")
        Faction.Print(self)
        
    
 
    
class Dwarves(Faction):
    
    __doc__= "Dwarves Class"
    
    firstEnemy = OrcsArmy          #Orcs
    secondEnemy = ElvesArmy        #Elves 
    
    def __init__(self):
        pass

    def PerformAttack(self, factionI, factionII):
        
        if Dwarves.firstEnemy.isAlive == True and Dwarves.secondEnemy.isAlive == True:
            Dwarves.firstEnemy.totalHealth -= (DwarvesArmy.numberUnits / 2) * DwarvesArmy.attackPoint
            Dwarves.secondEnemy.totalHealth -= (DwarvesArmy.numberUnits / 2) * DwarvesArmy.attackPoint
            
            factionI.ReceiveAttack(Dwarves.firstEnemy.receiveAttack, Dwarves)
            factionII.ReceiveAttack(Dwarves.secondEnemy.receiveAttack, Dwarves)
            
            return print("İki Düşman Hayatta")
        
        elif Dwarves.firstEnemy.isAlive == True and Dwarves.secondEnemy.isAlive == False:
            Dwarves.firstEnemy.totalHealth -= DwarvesArmy.numberUnits * DwarvesArmy.attackPoint
            factionI.ReceiveAttack(Dwarves.firstEnemy.receiveAttack, Dwarves)
            return print("Bir Düşman da Öldü")
        
        elif Dwarves.firstEnemy.isAlive == False and Dwarves.secondEnemy.isAlive == True:
            Dwarves.secondEnemy.totalHealth -= DwarvesArmy.numberUnits * DwarvesArmy.attackPoint
            factionII.ReceiveAttack(Dwarves.secondEnemy.receiveAttack, Dwarves)
            return print("Bir Düşman Hayatta") 
     
        else:
            return print("İki Düşman da Ölü")
    
    def ReceiveAttack(self, receiveAttack, faction):
        DwarvesArmy.numberUnits -= receiveAttack / DwarvesArmy.healthPoint
        return print("Dwarves Saldırı Aldı")
        
    def Print(self):
        print("“Taste the power of our axes!”")
        Faction.Print(self)
        
        

class Elves(Faction):
    
    __doc__= "Elves Class"
    
    firstEnemy = OrcsArmy            #Orcs
    secondEnemy = DwarvesArmy        #Dwarves 
    
    def __init__(self):
        pass
    
    def PerformAttack(self, factionI, factionII):
        
        if Elves.firstEnemy.isAlive == True and Elves.secondEnemy.isAlive == True:
            Elves.firstEnemy.totalHealth -= ((Elves.numberUnits * 60) / 100) * Elves.attackPoint
            Elves.secondEnemy.totalHealth -= ((Elves.numberUnits * 40) / 100) * ((Elves.attackPoint * 150) / 100)
            
            factionI.ReceiveAttack(Elves.firstEnemy.receiveAttack, Elves)
            factionII.ReceiveAttack(Elves.secondEnemy.receiveAttack, Elves)
              
            return print("İki Düşman Hayatta")
        
        elif Elves.firstEnemy.isAlive == True and Elves.secondEnemy.isAlive == False:
            Elves.firstEnemy.totalHealth -= Elves.numberUnits * Elves.attackPoint
            factionI.ReceiveAttack(Elves.firstEnemy.receiveAttack, Elves) 
            return print("Bir Düşman da Öldü")
        
        elif Elves.firstEnemy.isAlive == False and Elves.secondEnemy.isAlive == True:
            Elves.secondEnemy.totalHealth -= Elves.numberUnits * ((Elves.attackPoint * 150) / 100)
            factionII.ReceiveAttack(Elves.secondEnemy.receiveAttack, Elves)
            return print("Bir Düşman Hayatta") 
     
        else:
            return print("İki Düşman da Ölü")
        
    def ReceiveAttack(self, receiveAttack, faction):
        
        if faction == Orcs:
            receiveAttack = (receiveAttack * 125) / 100
        
        elif faction == Dwarves:
            receiveAttack = (receiveAttack * 75) / 100
        
        else:
            print("Saldırı Yok")
      
        ElvesArmy.numberUnits -= receiveAttack / ElvesArmy.healthPoint 
        return print("Elves Saldırı Aldı")
    
    def Print(self):
        print("“You cannot reach our elegance.”")
        Faction.Print(self)
    
    
    
Orcs = Orcs()
Dwarves = Dwarves()
Elves = Elves()

Orcs.PerformAttack(Dwarves, Elves)


