import re

input = "Hello, World!"
pattern = r"\b\w+\b"

replaced = re.sub(pattern, "Hi", input)
split = re.split(pattern, input)

print(replaced)  # Output: "Hi, Hi!"
print(", ".join(split))  

# Output: "Hello, World"