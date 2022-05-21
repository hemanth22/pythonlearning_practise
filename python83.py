## Polymorphism

class User(object):
    def sign_in(self):
        print('Logged In')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Merlin',50)
archer1 = Archer('Robin',50)

def player_attack(hello):
    hello.attack()

player_attack(wizard1)
player_attack(archer1)
