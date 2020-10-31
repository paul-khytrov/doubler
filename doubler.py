a = input("Введіть слово")#boom
b = ""
for i in range(len(a)):
    if a[i]!=" ":
        b = b + a[i]*2
    else:
        b = b + a[i]
print(b)
