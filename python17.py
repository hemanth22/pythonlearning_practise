## Built-in Functions + Methods

# Refer to python built functions url: https://docs.python.org/3/library/functions.html
# Refer to string methods url: https://www.w3schools.com/python/python_ref_string.asp
print(len('hellloooo'))

greet = 'hellloooo'
print(greet[0:len(greet)])


quote = 'to be or not to be'
print(quote.upper())

print(quote.capitalize())

print(quote.lower())

print(quote.find('be'))

print(quote.replace('be','me'))

print(quote)

quote2 = quote.replace('be','me')
print(quote2)
print(quote)