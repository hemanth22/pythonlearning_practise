# excercise
class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList();

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list)) ## This will give will give whether the superlist is issubclass of list
print(issubclass(list, object )) ## This will give whether the list is issubclass of object
