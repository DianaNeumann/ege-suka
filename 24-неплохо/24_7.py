f = open('k8-0.txt')
s = f.readline()

kmax = 1
k = 1

ch = 0

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        k += 1
        if k > kmax:
            kmax = k
            ch = s[i]
    else:
       k = 1
print(ch, kmax)
