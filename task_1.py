dog_name = input("Как зовут вашу собаку? ")
dog_age = input('Введите возраст вашей собаки в годах: ')

if int(dog_age) < 1:
    print("Формула не применима")
else:
    result = int(dog_age) * 7
    print("Человеческий возраст вашей собаки", dog_name, "-", result)