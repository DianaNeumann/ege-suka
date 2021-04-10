s = open('24-j9.txt').read()

k = 0
for i in range(0, len(s) // 2):
    if s[i] == s[-i-1]:

        k += 1

print(k)
