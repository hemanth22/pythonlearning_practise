class PlayerCharacter:
    def __init__(self, name, age):
        # self = name This is for parameter in class
        self.name = name # This is to make parameter in class and make dynamic output access
        self.age = age
    
    def run(self):
        print('run')
        return 'done'
    
player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print("Player 1 Age: ",player1.age)
print("Player 2 Age: ",player2.age)
print("Player 1 Function: ", player1.run())

# print(player1.attack) AttributeError: 'PlayerCharacter' object has no attribute 'attack'
print("Player 2 attribute: ",player2.attack)

help(list)
