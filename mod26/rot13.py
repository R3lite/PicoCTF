code = input("Enter code: ")
shift = int(input("Enter shift: "))
for letter in code:
    letter_in_ascii = ord(letter)
    if 97 > ord(letter.lower()) or ord(letter.lower()) > 122:
        print(letter, end="")
        continue
    if letter.lower() == letter:
        algo = (letter_in_ascii - 97 + shift) % 26 + 97
    else:
        algo = (letter_in_ascii - 65 + shift) % 26 + 65

    print(chr(algo), end="")
