import re

def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'[0-9]', password):
        return False

    if not re.search(r'[!@#№%^&?*]', password):
        return False
    return True


print("Требования к паролю:\n 1.Не менее 8 символов\n 2.Присутствие символов верхнего и нижнего регистра\n 3.Хотя бы одна цифра\n 4.Один или более специальных символов")

while True:
    passw = input("Введите новый пароль: ")
    if is_strong_password(passw):
        print("\033[32mПароль надёжный.\033[0m")
        break
    else:
        print("\033[31mПароль не соответствует требованиям. Попробуйте ещё раз.\033[0m")
#optimize
