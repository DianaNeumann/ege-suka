s = open('k7c-1.txt').read()

arr = 'BCD'
arr2 = 'BDE'
arr3 = 'BCE'

ans = 0

for i in range(0, len(s) - 2 ):
    if s[i] in arr:
        if (s[i+1] in arr2) and (s[i+1] != s[i]):
            if (s[i+2] in arr3) and (s[i+2] != s[i+1]):
                ans += 1

print(ans) 
