n = int(input('enter the answer of Olya: '))
for i in range(1, 101):
    n /= 2
    if n == 1:
        print('верно')
        break
if n != 1:
    print('неверно')