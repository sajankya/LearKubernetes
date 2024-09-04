class Monster:
    # Attributes
    health = 90
    energy = 40
    
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy

    #methods 
    def attack(self,name,age,health):
        print(f'Default health is {self.health}')  ### Classed attribute health passed  
        print(f'Name is {name}')
        print(f'Age is {age}')
        print(f'Passed health is {health}')  ## method attribute health passed

    def move(self,speed):
        print(f'Default energy is {self.energy}')
        print(f'speed is {speed}')
        speed -= 10
        print(f'Speed is reduced by 10 and new speed is {speed}')
        

monster = Monster(10,50)
#print(monster.health)
monster.attack("Sajan",37,"good")
monster.move(80) 

