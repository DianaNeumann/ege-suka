def find_prime(n):
    k = 0
    d = 2

    while d * d <= n:
        if n % d == 0:
            k += 2
        d += 1

    if k == 0:
        return True

    else:
        return False
    
    



for i in range(2943444, 2943529):
    if find_prime(i) == True:
        print(i, end=" ")

