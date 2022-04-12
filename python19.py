## Exercise: Type Conversion

name = 'Andrei Neagoie'
ages = 50
relationship_status = 'single'

relationship_status = 'it\'s complicated'

print(relationship_status)

birth_year = input('What year were you born?')
print(type(birth_year))

age = 2019 - float(birth_year)
print(f'You are {age} years old')
