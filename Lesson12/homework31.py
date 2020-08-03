def newfunc(osman):
    def myfunc(clon):
        return osman + clon
    return myfunc
a = newfunc(2)
print(a(2))