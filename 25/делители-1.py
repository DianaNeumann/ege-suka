def f (n):
    x = []
    d = 2               # первый делитель = 2  
    while d * d < n:
        if n % d == 0:
            x.append(d)
            x.append(n // d)
            if len(x) > 2:
                break
        d += 1
    d += 1
    return x

for i in range(289123456, 389123456 + 1): # 100 000 000 чисел
    a = []
    if i**0.5 == int(i**0.5):
        a = f(i)
        if len(a) == 2:
            print(i, a[1])
