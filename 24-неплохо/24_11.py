import re

s = open('24-s1.txt').read()

s = s.split()


ans = 0
for i in range(0, len(s)):
    if re.findall(r'(F.O)+', s[i]) != []:
        ans += 1

print(ans)
