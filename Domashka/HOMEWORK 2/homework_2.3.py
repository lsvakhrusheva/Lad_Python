age = int(input("Сколько тебе лет? "))

if 0 > age or age >= 150:
    print("Введите корректное число от 0 до 149")
elif age >= 65:
    print("Пенсионер")
elif age >= 18:
    print("Взрослый")
elif age >= 13:
    print("Подросток")
else:
    print("Ребенок")
