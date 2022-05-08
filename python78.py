# Abstraction
class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name # protected 
        self._age = age
        #self.__age = age # private
    
    def run(self):
        print('run')
    
    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} year old')

player1 = PlayerCharacter('andrei',100)
print(player1.speak)
