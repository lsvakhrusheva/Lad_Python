secret_number = 5

for item in range(6,21):
    if item == secret_number:
        print ("Нашли")
        break #программа останавливается, в случае если if item == secret_number= true? если false, то идет дальше

else:
    print ("Не нашли")
