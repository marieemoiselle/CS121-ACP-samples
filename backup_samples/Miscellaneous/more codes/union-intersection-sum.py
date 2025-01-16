set1 = set(map(int, input("Enter elements of the first set: ").split()))
set2 = set(map(int, input("Enter elements of the second set: ").split()))

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Sum of Union:", sum(union_set))
print("Sum of Intersection:", sum(intersection_set))