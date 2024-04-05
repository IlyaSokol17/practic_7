n = int(input('enter maximum volume: '))
x = int(n ** (1 / 3)) + 1
for i in range(1, x):
    print(i ** 3, end = ' ')
    