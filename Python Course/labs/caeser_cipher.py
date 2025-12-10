input_text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))

output_text = ""
for char in input_text:
    if char.isalpha():
        ascii_offset = 65 if char.isupper() else 97
        output_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
    else:
        output_text += char

print(output_text)
