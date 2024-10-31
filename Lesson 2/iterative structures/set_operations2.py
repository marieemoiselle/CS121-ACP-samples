set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

diff = set1 - set2
diff2 = set2 - set1
union_set =  set1 | set2
sd1 = set2 ^ set1
sd2 = set1 ^ set2
in1 = set1 & set2
in2 = set2 & set1

print(f"set1: {set1}")
print(f"set2: {set2}")

print("----- SET OPERATIONS -----")

print(f"set1 - set2 = {diff}")
print(f"set2 - set1 = {diff2}")
print(f"set1 | set2 = {union_set}")
print(f"set2 ^ set1 = {sd1}")
print(f"set1 ^ set2 = {sd2}")
print(f"set1 & set2 = {in1}")
print(f"set2 & set1 = {in2}")


"""
set1 – set2
set2 – set1
set1 + set2
set2 ^ set1
set1 ^ set2
set1 & set2
set2 & set1

"""