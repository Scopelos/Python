with open("problem_5.txt", "w") as f:
    number_string = input("Введите целые числа, разделенные пробелами: ")
    f.write(number_string)

data = []
with open("problem_5.txt") as f:
    for line in f:
        data.append([int(x) for x in line.split()])

data_sum = []
for el in data:
    data_sum = data_sum + el
print("Сумма чисел равна: ", sum(data_sum))










