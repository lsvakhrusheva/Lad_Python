name = input("Как тебя зовут? ")
try:
    age = int(input("Сколько тебе лет? "))
except ValueError:
    print("Это не число")
    age=0

age_next_year = age+1

print(f"Привет, {name}. Ты в курсе, что тебе в следующем году будет уже {age_next_year}?")


height = 1.6
favorite_number = 3
love_python = True

print (age, height, favorite_number, love_python)

print(type(age))
print(type(height))
print(type(favorite_number))
print(type(love_python))

age_in_days=int(age*365)
print(f"Твой возраст в днях {age_in_days}")








