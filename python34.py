## Dictionary Methods
##referemce url: https://www.w3schools.com/python/python_ref_dictionary.asp

users = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}
print(users.get('age', 55)) # If age does not exists it will override with 55

users2 = dict(name='JohnJohn')
print(users2)
