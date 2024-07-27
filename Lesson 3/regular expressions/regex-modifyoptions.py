import re

input = "Hello, World!"
pattern = r"hello"

is_match = re.search(pattern, input, re.IGNORECASE)
print(is_match)  

# Output: <re.Match object; span=(0, 5), match='Hello'>