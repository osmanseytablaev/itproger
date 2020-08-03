d = {"Один" : "Питон", "Два" : "C++", "Три" : "Java", "Четыре" : "C#"}
osman = d.copy()
print(osman)
d.clear()
osman.pop("Три")
print(osman)
osman['Новое']='Kotlin'
print(osman)
