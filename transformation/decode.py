def decode_letter(letter):
    first = chr(ord(letter) >> 8)
    second = chr(ord(letter) - (ord(first) << 8))
    return first+second

encoded = input("Enter encoded message: ")
for letter in encoded:
    print(decode_letter(letter), end='')

