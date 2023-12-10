#question to import lines
x = input("Enter line: ")
with open("text.txt","a+") as f:
    
    f.write(f"{x}/n")
    while True:
        y = int(input("1 to add more, 2 to read, 3 to quit: "))
        f.seek(0)
        if y == 1:
            z = input("Enter line: ")
            f.write(f"{z}/n")
        elif y == 2:
            f.read()
        elif y == 3:
            quit()