# Write a python script to read a plain text and convert it into a cipher text by shifting characters with value n

def cipher(old_str, val):
    new_str = []
    for i in old_str:
        temp = ord(i)
        temp += val
        temp = chr(temp)
        new_str.append(temp)
    return new_str

new = cipher("Hello",4)
print(new)
