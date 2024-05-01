import sys

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha() and char.isupper():
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
    return encrypted_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python caesar_cipher.py <shift>")
        sys.exit(1)
    
    try:
        shift = int(sys.argv[1]) % 26
    except ValueError:
        print("Error: Shift must be an integer")
        sys.exit(1)

    for line in sys.stdin:
        message = line.strip().upper()
        encrypted_message = caesar_cipher(message, shift)

        for i in range(0, len(encrypted_message), 5):
            print(encrypted_message[i:i+5], end=" ")

if __name__ == "__main__":
    main()
