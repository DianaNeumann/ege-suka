def is_prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def two_prime(n):
    a = 0
    d = 2

    while d * d <= n:
        if is_prime(d) == True:
            if n % d == 0:
                if is_prime(n//d):
                    if d != (n//d):
                        a += 1

            d += 1
        else:
            d += 1

    return a




max_a = 0
b = 0
for i in range(125697, 190234 + 1):
    if two_prime(i) != 0:
        b += 1
        if i > max_a:
            max_a = i

print(b, max_a)
