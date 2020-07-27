N = int(input("Введите число: "))
some = [9, "Hi", 23.5, "A"]
lis = []
while N > 0:
    lis.append (input("Введи что-то: "))
    N -= 1
some.extend(lis)
print(some)
    
        
    
    