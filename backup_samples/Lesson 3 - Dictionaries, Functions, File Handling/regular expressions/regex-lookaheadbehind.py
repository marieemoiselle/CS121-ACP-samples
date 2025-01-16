import re

input = "apple orange banana"
pattern = r"\b\w+(?= orange\b)"

match = re.search(pattern,

input)

print(match.group())  

# Output: "apple"