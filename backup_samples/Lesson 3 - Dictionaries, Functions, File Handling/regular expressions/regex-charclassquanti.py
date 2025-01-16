import re

input = "marie"
pattern = r"[aeiou]+"
match = re.search(pattern, input)
print(match.group()) 

# Output: "a"