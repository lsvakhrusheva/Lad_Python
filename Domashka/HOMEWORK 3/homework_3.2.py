stop_number = 0
total = 0

while True:
    n = int(input("Введите целое число: "))
    total += n

    if n != 0:
        print (n)
        continue
    if n == 0:
        print (total)
    break

