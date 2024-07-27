import re

email = "fatimamarie@gmail.com"
pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

is_valid = re.match(pattern, email)
print(is_valid)  

# Output: <re.Match object; span=(0, 19), match='fatimamarie@gmail.com'>