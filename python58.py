#parameters

#default parameters
def say_hello(name='Darth Vader', emoji='🤖'):
    print(f'Helloooo {name} {emoji}')

# without arguments
say_hello()

# positional arguments
say_hello('Andrei', '😃')

# keyword arguments
say_hello(name='Hemanth', emoji='😃')