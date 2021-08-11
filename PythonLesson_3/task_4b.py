def my_func(x,y):
    x = int(input("Введите целое положительное число: "))
    y = abs(int(input("Введите целое отрицательное число: ")))
    z = 1
    for i in range(y):
        z = z*x
    return z

print(my_func("", ""))


