def is_prime(n):
    d = 2 
    while d * d <= n:
        if n % d == 0:
            return False

        d += 1

    return True


def sum_p(n):
    a = []
    s = 0

    n = str(n)
    for i in n:
        a.append(int(i))
    
    return sum(a)





for i in range(33333, 55555 + 1):
    if is_prime(i) == True:
        if sum_p(i) > 35:
            print(i, sum_p(i), end=" ")
