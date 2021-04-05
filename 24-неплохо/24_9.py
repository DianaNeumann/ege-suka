f = open('24-j5.txt')
s = f.readline()

k = 0
k1 = 0

for i in range(len(s) - 2):
    if s[i] == 'O' and s[i+1] == 'C' and s[i+2] == 'K':
        k += 1

for i in range(len(s) - 4):
    if s[i] + s[i+1] + s[i+2] + s[i+3] + s[i+4] == 'STOCK':
        k1 += 1

print(k - k1)
