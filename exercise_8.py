n = int(input('загадайте натуральное число: '))
k = 0
while n > 1:
    n /= 2
    k += 1
print(k)

