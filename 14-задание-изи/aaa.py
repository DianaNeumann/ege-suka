n = 729**7 + 3**16 - 18


a = ''

while n > 1:
    a = str(n % 9) + a
    n =  n // 9

print(str(a).count('0'))
