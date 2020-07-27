import sys

while True:
    calculate = input("comand1: +,   comand2: -,   comand3: *,   comand4 /: ")
    if calculate == "+":
        calculateOne = int(input("Введите первое число для сложения: "))
        calculateExtra1 = int(input("Введите второе число для сложения: "))
        res1 = calculateOne + calculateExtra1
        print(res1)
    if calculate == "-":
        calculateTwo = int(input("Введите первое число для вычитания: "))
        calculateExtra2 = int(input("Введите второе число для вычитания: "))
        res2 = calculateTwo - calculateExtra2
        print(res2)
    if calculate == "*":
        calculateThree = int(input("Введите первое число для умножения: "))
        calculateExtra3 = int(input("Введите второе число для умножения: "))
        res3 = calculateThree * calculateExtra3
        print(res3)
    if calculate == "/":
        calculate4 = int(input("Введите первое число для деления: "))
        calculateExtra4 = int(input("Введите второе число для деления: "))
        res4 = calculate4 / calculateExtra4
        print(res4)
    else:
        print("Its didnt comand!!!")
    replay = input("Want to continue? ").lower()
    print(replay)
    if replay in ("yes", "y"):
        continue
    elif replay in ("no", "n"):
        raise SystemExit
    else:
        print("Sorry, I didn't understand that.")
