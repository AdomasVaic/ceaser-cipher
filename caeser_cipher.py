key = 5
def encrypt(n, text):
    out = []
    for char in text:
        cipher = ord(char) + n
        if cipher > ord("Z"):
            cipher = cipher - 26
        if cipher == ord(" ") + n:
            cipher = cipher - n
        cipher = chr(cipher)
        out.append(cipher)
    output = "".join(out)
    return output

def decrypt(n, encrypted_text):
    out = []
    for char in encrypted_text:
        plain = ord(char) - n
        if char == " ":
            plain = chr(plain)
            plain = " "
            plain = ord(plain)
        if ord(" ") < plain < ord("A"):
            plain = plain + 26
        plain = chr(plain)
        out.append(plain)
    output = "".join(out)
    return output

a = encrypt(key, "SIAURES PIETUS")
print(a)

b = decrypt(key, a)
print (b)


