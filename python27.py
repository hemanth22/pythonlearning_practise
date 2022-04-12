## list methods 3

basket = ['a', 'b', 'c', 'd', 'e','d']
basket.sort()
print(basket)
new_basket = ['x','a', 'b', 'c', 'd', 'e','d']
print(sorted(new_basket))

new_basket1 = new_basket[:]
new_basket1.sort()
print(new_basket1)

new_basket2 = new_basket.copy()
new_basket2.sort()
print(new_basket2)

new_basket.reverse()
print(new_basket)
