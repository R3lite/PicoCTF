message = input("Enter message to encode: ")
print(''.join([chr((ord(message[i]) << 8) + ord(message[i + 1])) for i in range(0, len(message), 2)]))
