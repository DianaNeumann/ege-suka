import re

f = open('24-1.txt')
s = f.readline()


k = re.findall(r'[0123456789]+', s)

ans = 0

for i in range(0,len(k)):
    k[i] = int(k[i])

for i in k:
    if i % 2 != 0 and i > ans:
        ans = i
    

print(ans)
