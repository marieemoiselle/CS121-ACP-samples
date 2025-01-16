import re

input = "Fatima Marie"
pattern = r"mari"
is_match = re.search(pattern, input, re.IGNORECASE)
print(is_match)  

# Output:
# <re.Match object; span=(7, 12), match='Marie'>