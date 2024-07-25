my_set = {1, 2, 3, 4}

#Using remove
my_set.remove(3)
print(my_set)

#Using discard
my_set.discard(5)  # No error if element not present
print(my_set)

#Using pop
popped_element = my_set.pop()  # Removes and returns an arbitrary element
print(my_set)