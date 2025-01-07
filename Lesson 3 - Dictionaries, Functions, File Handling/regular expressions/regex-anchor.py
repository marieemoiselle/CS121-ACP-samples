import re

input = "Bonjour, world!"
pattern = r"^Bonjour"

is_match = re.search(pattern, input)
print(is_match)

# Output:
# <re.Match object; span=(0, 7), match='Bonjour'>