def my_func(x,y,z):
    x = int(input("Введите число: "))
    y = int(input("Введите число: "))
    z = int(input("Введите число: "))
    a = [x,y,z]
    b = sorted(a)
    return b[-1] + b[-2]
print(my_func("", "", ""))

