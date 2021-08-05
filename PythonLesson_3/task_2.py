def u_data(u_name, u_tel):
    u_name = input("Введите ваше имя: ")
    u_tel = input("Введите ваш телефон: ")
    return u_name, u_tel

print(u_data("", ""))

user_name, user_tel = u_data
print(f"Имя пользователя - {user_name}; Телефон пользователя - {u_data}")