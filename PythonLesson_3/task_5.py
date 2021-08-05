def my_func_1():
    a = input("Введите несколько целых чисел через пробел: ")
    b = map(int, input(a).split())
    print(b)
    for x in b:
        c = sum(x)
    return c

print(my_func_1())
