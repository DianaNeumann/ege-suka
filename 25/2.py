def find_del(n):
    a = set()
    a.add(1)
    k = 1
    d = 2

    while d * d <= n:            
        if n % d == 0:
            k += 2
            # print(d)
            a.add(d)
            # print(n // d)
            a.add(n // d)
        d += 1


    return list(a)





ans = 0
for i in range(2, 20000 + 1):
    k = find_del(i)
    k = sum(k)
    if k > i:
        ans +=1

print(ans)
