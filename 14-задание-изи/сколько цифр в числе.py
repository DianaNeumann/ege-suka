n = 81 ** 15 + 3 ** 22 - 27 # сколько цифр 8 в 9ричной записи этого числа

k8 = 0
while n > 0 :
    if n % 9 == 8:
        k8 += 1
    n = n // 9

print(k8)

# OUTPUT
# 9
