plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

ciphertext = ""
for i, c in enumerate(plaintext):
    k = key[i % len(key)]
    
    c_pos = ord(c.lower()) - ord('a')
    k_pos = ord(k.lower()) - ord('a')
    
    new_c = (c_pos + k_pos) % 26
    new_c = chr(new_c + ord('a'))
    
    new_c = new_c if c.islower() else new_c.upper()
    ciphertext += new_c
    
print(f"Ciphertext: {ciphertext}")