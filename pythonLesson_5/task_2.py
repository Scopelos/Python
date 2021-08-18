count = 0
with open(r"problem_2.txt", "r") as sth:
    for line in sth:
        count = count +1
        print(count)


with open(r"problem_2.txt", "r") as sth:
    text = sth.read()
    words = text.split()


print("Число слов в тексте составляет ", len(words))



