f = open('k7a-5.txt')
import re
s = f.readline()


k = re.findall(r'[ABED]+',s)
print(k)

m = 0
for i in range(0, len(k)):
    m = max(m, len(k[i]))

print(m)
