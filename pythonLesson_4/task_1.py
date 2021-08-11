from sys import argv

script_name, productivity, rate, bonus = argv

print(script_name)
print(productivity)
print(rate)
print(bonus)

a = int(productivity)
b = int(rate)
c = int(bonus)

def my_funct(a,b,c):
    d = int(a*b + c)
    return d

print("Заработная плата сотрудника составляет ", my_funct(a,b,c), "у.е.")