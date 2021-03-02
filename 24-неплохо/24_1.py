f = open('24.txt','r')

line = f.readline()
a = [0] * 26 # массив с алфавитом

for i in range(1, len(line) - 1):
    if line[i-1] == line[i+1]:
        a[ord(line[i]) - ord('A')] += 1

print(max(a)) # => буква D
