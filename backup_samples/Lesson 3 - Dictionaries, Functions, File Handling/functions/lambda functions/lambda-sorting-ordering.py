fruits = ['peach', 'apple', 'mango', 'strawberry', 'banana']
sorted_fruits = sorted(fruits, key=lambda fruit: fruit[::-1])
print(sorted_fruits) 

 # Output: ['banana', 'apple', 'peach', 'mango', 'strawberry']