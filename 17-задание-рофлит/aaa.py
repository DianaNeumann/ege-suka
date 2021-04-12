def isprime(n):
    d = 2
    while d*d <= n:
        if n % d == 0:
            return 0

        d += 1
    return 1

def del3(n):
    k = 0
    d = 2
    while d*d < n:
        if n % d == 0:
            if isprime(d) == 1:
                k += 1

        d+=1

    if k == 3:
        return 1
    else:
        return 0



k = 0
for i in range(10001, 50001):
    if del3(i) == 1:
        k += 1

print(k)
