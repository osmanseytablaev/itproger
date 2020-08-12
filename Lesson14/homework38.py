f = open('example.txt', 'wt')
f.write('Привет')
f.close()
try:
    f = open('example.txt', 'x')
except FileExistsError:
    f = open('example.txt', 'a')
    print ("Oткрытие через 'a'")
finally:
    f.close()
