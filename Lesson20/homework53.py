def decorator(dec):
    def clon(osman):
        print('Код до выполнения функции')
        dec(osman)
        print('Код после выполнения функции')
    return clon
@decorator
def osman(os):
    print(os)
print('Hi')
    