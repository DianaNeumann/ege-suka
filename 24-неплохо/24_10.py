f = open('24-s2.txt')
s = f.readline()


arr = [0] * 26


for i in range(len(s)):
    if s[i] == 'X':
        index = ord(s[i+1]) - ord('A')
        arr[index] += 1
       

print(chr(ord('A') + 20) + str(max(arr)))
