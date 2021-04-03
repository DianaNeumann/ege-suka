print('x y z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            if (x <= z) and (y <= x) == True:
                print(x, y, z)
                
       
# output # 
# x y z
# 0 0 0
# 0 0 1
# 1 0 1
# 1 1 1
