## Dictionary
dictionary = {
    'a':1,
    'b':2,
    'x':3
}

print(dictionary['b'])
print(dictionary)

dictionary1 = {
    'a':[1,2,3],
    'b':'hello',
    'x':True
}

print(dictionary1)
print(dictionary1['a'][1])

my_list = [
    {
        'a': [1,2,3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4,5,6],
        'b': 'hello',
        'x': True
    }
]
print(my_list[0]['a'][2])