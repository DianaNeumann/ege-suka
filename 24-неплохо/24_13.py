s = open('k7-m23.txt').read()

a = []

for i in range(0, len(s) - 2):
    if not(s[i] > s[i+1]):
        if not(s[i+1] > s[i+2]):
            k = s[i] + s[i+1] + s[i+2]
            a.append(k)



print(len(a))
print(s.rfind(a[-1]))
