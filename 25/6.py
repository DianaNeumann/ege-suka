def is_prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def find_prime_del(n):
    k = 0 
    d = 2
    while d < n:
        if is_prime(d) == True:
            if n % d == 0:
                k += 1
        d += 1

    return k


ans = [0,0] 
for i in range(2,20000 + 1):
    a = find_prime_del(i) 
    if a > int(ans[0]):
        ans[0] = a
        ans[1] = i

print(ans)
        
