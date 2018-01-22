def shapeArea(n):
    sum = 1
    
    for i in range(n):
        sum = 4*i + sum
    
    return sum
    
# 1 -> 1+ 4 -> 1+4+8 -> 1+4+8+12->....
