with open("problem_4.txt") as f:
    content = f.readlines()

data = [item.split() for item in content]

data_digits = [i[-1] for i in data]

data_russian = ["Один", "Два", "Три", "Четыре"]

data_dict = {data_russian[i]:data_digits[i] for i in range(len(data_russian))}

with open('problem_4a.txt', 'w') as f:
    for key, val in data_dict.items():
        f.write('{}:{}\n'.format(key, val))

