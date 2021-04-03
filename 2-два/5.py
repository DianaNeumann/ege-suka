print('x y z w ')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if  x or (z and (not(w)))  or (y and (not(w))) or (y and (not(z)) ) == False:
                    print(x, y, z, w )
                    
           
 # output 
# x y z w 
# 0 0 0 0
# 0 0 0 1
# 0 0 1 0
# 0 0 1 1
# 0 1 0 0
# 0 1 1 0
# 0 1 1 1
# 1 0 0 0
# 1 0 0 1
# 1 0 1 0
# 1 0 1 1
# 1 1 0 0
# 1 1 0 1
# 1 1 1 0
# 1 1 1 1
