## *args and **kwargs

def super_func(*args):
    '''
    #print(args) # prints all arguments in tuple
    #print(*args)
    INFO: This is arguments function
    '''
    return sum(args)

print(super_func.__doc__)
print(super_func(1,2,3,4,5))

def super_func2(*args, **kwargs):
    '''
    INFO: This is kwargs function
    '''
    print(kwargs)
    return sum(args)

print(super_func2.__doc__)
print(super_func2(1,2,3, 4, 5, num1=5, num2=10))

def super_func3(*args,**kwargs):
    '''
    INFO: This is args and kwargs function
    '''
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func3.__doc__)
print(super_func3(1,2,3, 4, 5, num1=5, num2=10))


## Rule: params, *args, default params, **kwargs

def super_func4(name,*args,i='hi',**kwargs):
    '''
    ## Rule: params, *args, default params, **kwargs
    INFO: This function is written to match above RULE
    '''
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func4.__doc__)
print(super_func4('Andy',1,2,3,4,5, num1=5, num2=10))