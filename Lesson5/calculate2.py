import sys
#My variant
while True:
    calculate = input("comand1: +,   comand2: -,   comand3: *,   comand4: /")
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
        print(calculate4 / calculateExtra4 if calculateExtra4 != 0 else "Нельзя делить на ноль!!!")    
    else:
        print("Sorry, I didn't understand that.")
    replay = input("Want to continue? ").lower()
    print(replay)
    if replay in ("yes", "y"):
        continue
    elif replay in ("no", "n"):
        raise SystemExit
#They variant
# #a = float (input ("Первое число: "))
# #b = float (input ("Первое число: "))
# #math_symbol = input ("Математическое действие: ")
# #if (math_symbol == "+"):
#     print ("Получается: ", a + b)
# elif (math_symbol == "-"):
#     print ("Получается: ", a - b)
# elif (math_symbol == "*"):
#     print ("Получается: ", a * b)
# elif (math_symbol == "/"):
#     print ("Получается: ", a / b if b != 0 else 'Нельзя делить на ноль!')
# else:
#     print ("Вы ввели что-то не то!")