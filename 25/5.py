def find_prime_7(n):
    k = 0
    d = 2

    while d * d <= n:
        if n % d == 0:
            k += 2
        d += 1

    if (k == 0) and (n % 10 == 7):
        return True

    else:
        return False
    
    



for i in range(2532000, 2532160):
    if find_prime_7(i) == True:
        print(i, end=" ")
