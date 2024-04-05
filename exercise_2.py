s = input('введите любую строку ')
a = ''
for i in range(2, len(s), 3):
    a += s[i]
print(a)