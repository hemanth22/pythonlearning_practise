# string indexes

selfish = 'me me me'
        #  01234567
print(selfish[7])
print(selfish)
# [start:stop]
print(selfish[0:2])
# [start:stop:stepover]
print(selfish[0:8:2])
# [start:]
print(selfish[1:])
# [:end]
print(selfish[:5])
# [::end]
print(selfish[::1])
# [-1] This will do reverse
print(selfish[-1])
# [::-1] Reverse an order or string
print(selfish[::-1])