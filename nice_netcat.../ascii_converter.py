with open("./out.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(chr(int(line)), end="")
