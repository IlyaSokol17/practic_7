n, k, r = map(int, input('введите длину нити(n), процент(k), минимальная финальная длина нити(r): ').split())
s = 1
while n < r:
    n = n + n * ((k/100))
    s += 1

print(s)
