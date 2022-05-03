# Exercise: check for duplicates in list:

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

## duplicates = set([x for x in some_list if some_list.count(x) > 1])

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

singleduplicates = []
singleduplicates = [ values for values in some_list if some_list.count(values) > 1 if values in singleduplicates]
print(singleduplicates)