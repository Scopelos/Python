with open("problem_3.txt") as f:
    content = f.readlines()

data = [item.split() for item in content]

salaries = []

for item in data:
    salaries.append([int(item[1]), item[0]])

salaries_sum = 0
for item in salaries:
    if item[0] < 20000:
        print(item[1])
    salaries_sum += item[0]

print("Средняя зарплата в компании:", round(salaries_sum / len(salaries)))
print("Была использована помощь зала")