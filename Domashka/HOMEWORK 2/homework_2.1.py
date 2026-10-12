number = int(input("Введите целое число: "))

if number % 2 == 1:
    print("Вы ввели нечетное число.")
else:
    print("Вы ввели четное число.")

positive_number = number > 0
negative_number = number < 0

if positive_number:
    print("Число положительное.")
elif negative_number:
    print("Число отрицательное.")
else:
    print("Вы ввели ноль")


if number > 100:
    print("Число больше 100.")
else:
    number = None
