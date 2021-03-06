def Del(n, m):
    return n % m == 0

def Formula():
    return (((Del(x,36) and Del(x,42)) <= Del(x, A)) and ((A*(A - 25) < 25*(A+200))))

for A in range(1,1000):
    false_flag = 0 
    for x in range(1,1000):
        if Formula() ==  False:
            false_flag = 1
    if false_flag == 0:
        print(A)

######## OUTPUT #########
# 1
# 2
# 3
# 4
# 6
# 7
# 9
# 12
# 14
# 18
# 21
# 28
# 36
# 42
# 63
# 84
