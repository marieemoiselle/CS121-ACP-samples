my_tuple = (9, 18, 27)
# my_tuple[3] = 36
# print(my_tuple)

new_tuple = my_tuple + (5, 10, 15)
print(new_tuple)

# conversion
converted_list = list(new_tuple)
print(f"List before 32: {converted_list}")
converted_list.insert(2, 32)
converted_list.append(90)
print(converted_list)