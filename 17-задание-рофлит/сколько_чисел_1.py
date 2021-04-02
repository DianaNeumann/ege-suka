k = 0

for i in range(3 * 10**10, 5*10**10 + 1, 100000):
    if i % 11 == 0 and i % 17 != 0 and i % 23 != 0 and i % 41 != 0 and i % 103 != 0:
                        k +=1
            
    
print(k)
        
