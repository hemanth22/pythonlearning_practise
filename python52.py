for item in [1,2,3]:
    print(item)

print('====================')

i = 0
while i < len([1,2,3]):
    print(i)
    i += 1

print('====================')

my_list = [1,2,3]
for item in my_list:
    print(item)

print('====================')

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

print('====================')

while True:
    input('say something: ')
    break

print('====================')

while True:
    response = input('say something: ')
    if (response == 'bye'):
        break
    