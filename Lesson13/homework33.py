age = -2
while age <= 0:
    try:
        age = int(input("Введите возраст: "))
    except ValueError:
        print("Это не возраст!!!")