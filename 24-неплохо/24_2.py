k = 0

f = open('24.txt')

for line in f:
    if line.count('A') > line.count('E'):
        k += 1

print(k)
