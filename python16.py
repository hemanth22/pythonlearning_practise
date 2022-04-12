## Immutability

selfish = '01234567'

#selfish = 100
#print(selfish)

selfish = selfish + '8' # This will replace whole selfish data
print(selfish)

selfish[0] = '8'
#here there will be error, because strings are immutable