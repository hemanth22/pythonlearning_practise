class PlayerCharacter:
    # Class Object Attribute
    membership = True #This is static attribute
    def __init__(self, name, age):
        # self = name This is for parameter in class
        self.name = name # This is to make parameter in class and make dynamic output access
        self.age = age
    
    def shout(self):
        print(f'my name is {self.name}')
    
#    @classmethod
#    def adding_things(cls, num1, num2):
#        return num1 + num2
#print(PlayerCharacter.adding_things(2,3))

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)
    
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

player3 = PlayerCharacter.adding_things(10,20)
print(player3.age)