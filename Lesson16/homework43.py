from random import randint
a = 1
b = 20
attempt = 3
clon = randint(a, b)
while attempt > 0:
    attempt -= 1
    osman = int(input("Введите число от 1 до 20: "))
    if osman == clon:
        print("Вы угадали!")
        break
    if osman != clon:
        print("Вы не угадали!")
        print("У вас осталось попыток ", (attempt))   
    if osman > clon:
        print("Загаданное число меньше вашего")
        continue
    if osman < clon:
        print("Загаданное число больше вашего")
        continue