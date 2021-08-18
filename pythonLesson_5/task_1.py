with open("old_file.txt", "w") as f:
    while True:
        s = input("Введите строку:  ")
        if len(s) == 0:
            break
        f.write(s + "\n")





