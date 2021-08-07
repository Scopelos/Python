def my_func_1():
    a = list(map(int, input("Введите несколько целых чисел через пробел: ").split()))
    b = sum(a)
    return b
c = my_func_1()
print(c)

def my_func_2():
    d = list(map(int, input("Введите несколько целых чисел через пробел: ").split()))
    e = sum(d)
    return e
f = my_func_2()
print(f)

g = c + f
print(g)

print("Не получилось сделать последнее условие ни через break, ни через exception")
