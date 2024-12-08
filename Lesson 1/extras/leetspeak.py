s = input("Enter message: ")

conv = {
    'a': '4',
    'e': '3',
    'i': '1',
    'o': '0',
    's': '5',
    't': '7',
    'g': '6'
}

res = ""
for c in s:
    new_c = conv.get(c.lower(), c)
    res += new_c
    
print(f"New message: {res}")