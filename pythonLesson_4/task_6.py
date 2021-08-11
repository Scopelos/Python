from itertools import count
from itertools import cycle

for i in count(int(input("Введите целое число от 1 до 10: "))):

    if i > 12:
        break
    else:
        print(i)

a = 0
for i in cycle(input("Введите последовательность из 3-х символов: ")):
    if a > 15:
        break
    print(i)
    a = a + 1
