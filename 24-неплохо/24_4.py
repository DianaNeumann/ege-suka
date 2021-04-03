f = open('k7a-1.txt').read()
import re
k = re.findall(r'[ABC]+', f)

l_max = 0
for i in range(0, len(k)):
    if len(k[i]) > l_max:
        l_max = len(k[i])

print(l_max)
