seconds = int(input("Сколько секунд?"))

m,s = divmod(seconds, 60)
h,m = divmod(m,60)

print(f'{h:02d}:{m:02d}:{s:02d}')

print("Google нам в помощь")


