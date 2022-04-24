user = {
    'name': 'Golem',
    'age': 7,
    'can_swim': False
}

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for x,y in user.items():
    print(x,':',y)

for item in user.items():
    key,value = item;
    print(key,'=',value)

#iterable - list, dictionary, tuple, set, string
#iterate -> one by one check each item in the collection