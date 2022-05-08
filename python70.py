class PlayerCharacter:
    # Class Object Attribute
    membership = True #This is static attribute
    def __init__(self, name='anonymous', age=0):
        if (age > 18):
        # self = name This is for parameter in class
            self.name = name # This is to make parameter in class and make dynamic output access
            self.age = age
    
player1 = PlayerCharacter() # This will not return any value
player2 = PlayerCharacter('Tom', 21)
print('Player2 : ',player2.name)
#print('Player1 : ',player1.name) #This will throw an error
# help(list)
