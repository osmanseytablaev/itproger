try:    
    f = open('osman.txt', 'r')
except FileNotFoundError:
    print('Такого файла не существует!!!')