def Del(n, m):
    return n % m == 0

def Formula():
    return ((not Del(x, A) and Del(x, 21)) <= Del(x, 14))

for A in range(1,1000):
    false_flag = 0 
    for x in range(1,1000):
        if Formula() ==  False:
            false_flag = 1
    if false_flag == 0:
        print(A)

######## OUTPUT #########
# 
# 1
# 3
# 7
# 21  
