file = open('24.txt')
f = file.readline()

ans = 0

for i in range(1, len(f)):
    if f[i] != f[i-1]:
        ans += 1


print(ans)
