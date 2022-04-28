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
        
    def AssgnEnemies(self):
        print(self.isAlive)
        return
    
    def PerformAttack(self):
        return
    
    def ReceiveAttack(self):
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
        


firstEnemy = Faction("Faction_I",50,30,150,10)
secondEnemy = Faction("Faction_II",60,25,125,12)   
 


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
    
    
    
firstFaction = Merchant(10, 10, 360, 5, 6)
secondFaction = Merchant(12, 12, 300, 8, 9)
thirtFaction = Merchant(8, 8, 400, 7, 6)



class Orcs(Faction):
    
    __doc__= "Orcs Class"
    
    def __init__(self):
        pass
    
    def Print(self):  
        
        print("“Stop running, you’ll only die tired!”")
        Faction.Print(self)
    
    
    
class Dwarves(Faction):
    
    __doc__= "Dwarves Class"
    
    def __init__(self):
        pass

    def PerformAttack(self):
        
        if firstEnemy.isAlive == True and secondEnemy.isAlive == True:
            return print("İki Düşman Hayatta")
        
        elif firstEnemy.isAlive == False and secondEnemy.isAlive == False:
            return print("İki Düşman da Öldü")
        
        else:
            return print("Bir Düşman Hayatta")
        
    def Print(self):
        
        print("“Taste the power of our axes!”")
        Faction.Print(self)
        
        

class Elves(Faction):
    
    __doc__= "Elves Class"
    
    def __init__(self):
        pass
    
    def Print(self):
        print("“You cannot reach our elegance.”")
        Faction.Print(self)
    
    
    



