## List methods

# list method url : https://www.w3schools.com/python/python_ref_list.asp

basket = [1,2,3,4,5]
#print(len(basket))

# append
basket.append(100)
new_list = basket
new_lists = basket.append(101)
print(basket)
print(new_list)
print(new_lists)

basket.insert(4,104)
news = basket
print(news)

basket.extend([106])
new_lists5 = basket
print(new_lists5)

# pop

basket.pop()
basket.pop(0)
print(basket)

# remove

basket.remove(4)
print(basket)

# clear

basket.clear()
new_lists7 = basket
print(new_lists7)