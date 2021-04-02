a = [0]*66

a[1] = 1

for i in range(2, 21):
    a[i] += a[i-1]
    if i % 3 == 0:
        a[i] += a[i // 3]

for i in range(21, 66):
    a[i] += a[i-1]
    if i % 3 == 0 and i // 3 >= 20:
        a[i] += a[i // 3]

print(a[65])
