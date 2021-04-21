for i in range(87921, 88187 + 1):
    s = str(i)

    sum_s = 0
    mul_s = 1

    for j in s:
        sum_s += int(j)
        mul_s *= int(j)

    if (sum_s % 14 == 0) and (mul_s % 18 == 0) and mul_s != 0:
        print(sum_s, mul_s)
