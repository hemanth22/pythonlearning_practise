## Dictionary Methods 2
## url https://replit.com/@aneagoie/dictionary

user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}
print('basket' in user)
print('size' in user)
print('hello' in user.values())
print('hello' in user.items())
print(user.items())
user2 = user.copy()
user3 = user.copy()
user.clear()
print(user)
print(user2)

user2.pop('age')
print(user2)

print(user2.popitem())
print(user2)

print(user2.update({'age': 55}))
print(user2)