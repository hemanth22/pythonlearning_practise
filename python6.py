#bin

print(bin(5))
print(int('0b101', 2))


# Python3 program for implementation
# of int() function
num = 13
 
String = '187'
 
# Stores the result value of
# binary "187" and num addition
result_1 = int(String) + num
print("int('187') + 13 = ", result_1, "\n")
 
# Example_2
str = '100'
 
print("int('100') with base 2 = ", int(str, 2))
print("int('100') with base 4 = ", int(str, 4))
print("int('100') with base 8 = ", int(str, 8))
print("int('100') with base 16 = ", int(str, 16))

#Convert binary string to Python int base
# "111" taken as the binary string
binaryString = "111"
 
# Stores the equivalent decimal
# value of binary "111"
Decimal = int(binaryString, 2)
 
print("Decimal equivalent of binary 111 is", Decimal)
 
# "101" taken as the octal string
octalString = "101"
 
# Stores the equivalent decimal
# value of binary "101"
Octal = int(octalString, 8)
 
print("Decimal equivalent of octal 101 is", Octal)