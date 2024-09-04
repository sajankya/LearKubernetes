class Monster:
    # Attributes
    health = 90
    energy = 40
    
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy

#     #methods 
#     def attack(self,name,age,health):
#         print(f'Default health is {self.health}')  ### Classed attribute health passed  
#         print(f'Name is {name}')
#         print(f'Age is {age}')
#         print(f'Passed health is {health}')  ## method attribute health passed

#     def move(self,speed):
#         print(f'Default energy is {self.energy}')
#         print(f'speed is {speed}')
#         speed -= 10
#         print(f'Speed is reduced by 10 and new speed is {speed}')


        

# monster = Monster(10,50)
# #print(monster.health)
# #monster.attack("Sajan",37,"good")
# #monster.move(80) 

# #print(dir(monster))

# print(len('test'))

# print('test'.upper())

# def add(a,b):
#     return a + b
# class Test:
#     def __init__(self,add_fucntion):
#         self.add_function = add_fucntion

# test = Test(add_fucntion=add(5,3))
# print(test.add_function)

##############################################################################

# class Monster:
#     def __init__(self,func):
#         self.func = func


# class Attacks:
#     def bite(self):
#         print('This is bite')

#     def strike(self):
#         print('This is strike')

#     def slash(self):
#         print('This is slash')

#     def kick(self):
#         print('This is kick')


# monster = Monster(func = Attacks().bite)
# monster.func()

###############################################################
# class Monster:
#     def __init__(self,func):
#         self.func = func

#     def print(self, test):
#         self.test = test
#         print(f'This is {test} ')


# monster = Monster(func = Monster().print(test ='hello'))

# monster.func


###################################################################

# def update_health(amount):
#     #global health
#     monster.health += amount


# class Monster:
#     def __init__(self,health):
#         self.health = health
    
# monster = Monster(health = 100)

# # health = 100
# # print(health)
# update_health(20)
# # monster.health += 20
# print(monster.health)

################################################################


# class Monster:
#     def __init__(self,health,energy):
#         self.health = health
#         self.energy = energy

#     def update_energy(self,amount):
#         self.energy += amount

# monster = Monster(health = 100, energy = 50)

# monster.update_energy(20)
# print(monster.energy)


################################################################


# class Monster:
#     def __init__(self,health,energy):
#         self.health = health
#         self.energy = self.set_energy(energy)

#     def set_energy(self,energy):
#         new_energy  = energy * 2
#         return new_energy

# monster = Monster(health = 100, energy = 50)

# monster.set_energy(20)
# print(monster.energy)


###############################################################


# class Monster:
#     def __init__(self,health,energy):
#         self.health = health
#         self.set_energy(energy)

#     def set_energy(self,energy):
#         new_energy  = energy * 2
#         self.energy =  new_energy

# monster = Monster(health = 100, energy = 50)

# # monster.set_energy(20)
# print(monster.energy)

###############################################################

# class Monster:
#     def __init__(self,health,energy):
#         self.health = health
#         self.energy = energy
    
#     def get_damage(self,amount):
#         self.health -= amount
        

# class Hero:
#     def __init__(self,damage,monster):
#         self.damage = damage
#         self.monster = monster

#     def attack(self):
#         self.monster.get_damage(self.damage)

# monster = Monster(health = 100, energy = 50)

# monster.get_damage(10)

# print(monster.health)

# hero = Hero(20, monster)
# hero.attack()

# print(monster.health)


###################################################################################



# class Monster:
#     def __init__(self,health,energy):
#         self.health = health
#         self.energy = energy
    
#     def attack(self,amount):
#         print('The monster has attacked')
#         print(f'{amount} damage has made')
#         self.energy -= 20

#     def move(self,speed):
#         print('Monstsre has moved')
#         print(f'It has a speed of {speed}')


# class Shark(Monster):
#     def __init__(self,speed,health,energy):
#         Monster.__init__(self,health,energy)
#         self.speed = speed

#     def bite(self):
#         print('The shark has bitten')

#     def move(self):
#         print('The Shark has moved')
#         print(f'The speed of the shar is {self.speed}')


# shark = Shark(speed =120, health = 100, energy = 50)

# print(shark.speed)
# print(shark.health)
# shark.attack(80)
# print(shark.energy)
# shark.move()
# print(shark.speed)


###################################################################################


# class Monster:
#     def __init__(self,health,energy):
#         self.health = health
#         self.energy = energy
    
#     def attack(self,amount):
#         print('The monster has attacked')
#         print(f'{amount} damage has made')
#         self.energy -= 20

#     def move(self,speed):
#         print('Monstsre has moved')
#         print(f'It has a speed of {speed}')


# class Shark(Monster):
#     def __init__(self,speed,health,energy):
#         #Monster.__init__(self,health,energy)
#         super().__init__(health,energy)
#         self.speed = speed

#     def bite(self):
#         print('The shark has bitten')

#     def move(self):
#         print('The Shark has moved')
#         print(f'The speed of the shar is {self.speed}')


# shark = Shark(speed =120, health = 100, energy = 50)

# print(shark.speed)
# print(shark.health)
# shark.attack(80)
# print(shark.energy)
# shark.move()
# print(shark.speed)

###################################################################################

# class Monster:
#     def __init__(self,health,energy):
#         self.health = health
#         self.energy = energy
    
#     def attack(self,amount):
#         print('The moster has attacked')
#         print(f'The {amount} damage has made')

#     def move(self,speed):
#         print('The moster has moved')
#         print(f'It has the speed of {speed}')
#         print(f'This has health of {self.health}')
#         print(f'This has energy of {self.energy}')
        

# class Scorpion(Monster):
#     def __init__(self,poison_damage,scorpion_health,scorpion_energy):
#         super().__init__(health=scorpion_health,energy=scorpion_energy)
#         self.poison_damage = poison_damage

#     def attack(self):
#         print(f'Poison damage is {self.poison_damage}')



# monster = Monster(health =100, energy=50)

# scorpion = Scorpion(poison_damage=20, scorpion_health=200, scorpion_energy=25)

# print(scorpion.health)
# print(scorpion.poison_damage)
# print(scorpion.energy)

# monster.attack(10)
# scorpion.attack()
# scorpion.move(30)

##################################################################################################################


      



















































