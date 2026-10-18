login = input("Enter your login: ").strip()
password = input ("Enter your password (minimum 6 characters): ")
age = int(input ("Enter your age: "))
email = input ("Enter your email: ")

#выведите сообщение об ошибке для каждого случая: пустой логин, слишком короткий пароль, возраст меньше 18, невалидный email.
if not login:
    print("Error: Your login is empty. Please, enter your login and try again.") #Если логин не валиден, то программа дальше не проверяет. Аналогично для каждого условия.
elif len(password) < 6:
    print("Error: Your password is too short. It must be at least 6 characters ")
elif age < 18:
    print("Error: Your age is too low. It must be at least 18 years old")
elif "@" not in email or "." not in email: #Тут тоже замыкание, но другое. Если нет собаки, то точку он не пойдет проверять.
    print("Error: Your email is not valid.")
else:
    print(f"Welcome, {login}")
