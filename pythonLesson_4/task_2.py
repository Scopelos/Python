a = list(map(int, input("Введите несколько целых чисел через пробел: ").split()))
b = [j for i, j in zip(a, a[1:]) if j > i]
print(b)

print("'j' - это помощь Google'а, сначала долго мучилась с 'i'")

