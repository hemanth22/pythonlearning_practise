## Dunder Methods

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }
    
    def __str__(self): ## This is a dunder method that is used for method overriding
        return f'{self.color}'
    
    def __len__(self):
        return 5


#def __del__(self):
#    print('deleted')
 
    def __call__(self):
        return('yess??')

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red',0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
# del action_figure
print(action_figure()) ## This is for call dunder method
print(action_figure['name']) 

## reference: https://docs.python.org/3/reference/datamodel.html#special-method-names