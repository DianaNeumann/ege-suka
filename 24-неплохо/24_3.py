import re
f = open('k7-100.txt').read()

k = re.findall(r'C+', f)

print(len(max(k)))
