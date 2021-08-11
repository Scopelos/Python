from functools import reduce
a = [i for i in range(100,1001) if i%2==0]
print(a)

def my_func(prev_el, el):
    return prev_el * el

print("Произведение всех четных чисел списка равно", reduce(my_func, a))