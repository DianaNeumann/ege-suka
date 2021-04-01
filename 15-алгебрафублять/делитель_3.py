def Del(n, m):
    return n % m == 0

def Formula():
    return ((A < 50) and (not(Del(x, A))) <= ( Del(x, 10) <= (not(Del(x, 18) ))))

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
# 5
# 6
# 9
# 10
# 15
# 18
# 30
# 45
