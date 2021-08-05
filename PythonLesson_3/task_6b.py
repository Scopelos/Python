def int_func():
    text = input("Введите слово латинскими буквами: ")
    a = text.capitalize()
    return a
print(int_func())

def ext_func():
    text_1 = input("Введите несколько слов латинскими буквами: ")
    b = text_1.split()
    print(b)
    return b
    for x in b:
        print(int_func())
print(ext_func())