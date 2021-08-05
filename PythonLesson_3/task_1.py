def my_func():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = round(a / b)
        return c
    except ZeroDivisionError:
        print("Деление на ноль")

result = my_func()
print(result)