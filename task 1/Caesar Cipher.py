def caesar_cipher(text, shift, direction):
    result = ""
    
    if direction == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result

# User input
message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))
mode = input("Do you want to encrypt or decrypt? ").lower()

# Encrypt or Decrypt
output = caesar_cipher(message, shift_value, mode)
print(f"The result is: {output}")
