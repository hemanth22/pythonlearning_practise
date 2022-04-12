#list slicing
#string = 'helllooo'
#string[0:2:1]
# Exmaple: https://replit.com/@aneagoie/lists#main.py
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
# print(amazon_cart[0:2])

amazon_cart[0] = 'laptop'
# new_cart = amazon_cart[0:3]
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
