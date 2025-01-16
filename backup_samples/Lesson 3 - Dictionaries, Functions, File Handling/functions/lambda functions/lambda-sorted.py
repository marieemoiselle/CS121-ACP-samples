students = [('Clyden', 100), ('Sevi', 92), ('Kalix', 88), ('Hiro', 95)]
sorted_scores = sorted(students, key=lambda student: student[1], reverse=True)
print(sorted_scores)

# Output:
# [('Clyden', 100), ('Hiro', 95), ('Sevi', 92), ('Kalix', 88)]