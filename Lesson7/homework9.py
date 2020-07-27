bye = []

for i in range (5):
    bye.append(i * 5)

print(bye)
hi = []
hi.append(5) 
hi.append(-6) 
print(hi)
hi.extend(bye)
hi.sort()

print(hi)


