## Tuples 2
# https://www.w3schools.com/python/python_ref_tuple.asp

my_tuple = (1, 2, 3, 4, 5, 5)
mew_tuple = my_tuple[1:2]
print(mew_tuple)

x,y,z, *other = (1, 2, 3, 4, 5)
print(x,y,z,other)

print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))