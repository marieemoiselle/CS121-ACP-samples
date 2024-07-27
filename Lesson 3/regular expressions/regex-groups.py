import re

input = "Jerome, Fatima, Gerald, Arjonel, Maurice"
pattern = r"(\w+), (\w+), (\w+)"

match = re.search(pattern, input)
print(match.group(2))  

# Output: "Fatima"