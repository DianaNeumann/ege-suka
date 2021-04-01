# ? ? ? ? 
# 1 1   1
#   1   1
#   1   1

print("x y z w ")

for x in 1,0:
    for y in 1,0:
        for z in 1,0:
            for w in 1,0:
                if ( (x <= y) and (x or not(z)) ) and (x == (not(w))) == 1:
                    print(x, y, z, w)

# OUTPUT
# x y z w 
# 1 1 1 0
# 1 1 0 0
# 0 1 0 1
# 0 0 0 1

# ОТВЕТ: zywz
