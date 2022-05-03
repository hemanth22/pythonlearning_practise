# with return
print("With return function")
def sum(num1, num2):
    return num1 + num2

print(sum(4,5))

print("Without return function")
#without return
def inum(num23, num24):
    print('hiii')
    num23 + num24

print(inum(10,5))

print("With return recurrsive function1")
def sum(num11,num12):
    def another_func(num11, num12):
        return num11 + num12
    return another_func

total = sum(10,20)
print(total(10,20))


print("With return recurrsive function2")
def sum(num11,num12):
    def another_func(num11, num12):
        return num11 + num12
    return another_func(num11, num12)

ptotal = sum(11,31)
print(ptotal)

print("After return function is completed it will exits for example below")

print("With return recurrsive function2")
def sum(num11,num12):
    def another_func(num11, num12):
        return num11 + num12
    return another_func(num11, num12)
    return 5
    print('hello')

xtotal = sum(12,32)
print(xtotal)