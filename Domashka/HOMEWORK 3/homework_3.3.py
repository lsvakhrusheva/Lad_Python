scores = [95, 88, 60, 42, 100, 5]
#>= 90 — «отлично», >= 70 — «хорошо», >= 50 — «удовлетворительно», иначе — «неудовлетворительно»

for item in scores:
    if item >= 90:
        print ("exсellent")
    elif item >=70:
        print ("good")
    elif item >=50:
        print ("satisfactory")
    else:
        print ("impossible")