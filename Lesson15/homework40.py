with open('some.txt', 'w') as f:
    f.write('Hi')
with open('some.txt', 'r') as file:
    print(file.read())