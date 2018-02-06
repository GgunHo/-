def alternatingSums(a):
    sum_1, sum_2 = 0, 0
    b = []
    for i in range(len(a)):
        if (i+1) % 2 == 0 : 
            sum_2 += a[i]
        else :
            sum_1 += a[i]
    b.extend([sum_1,sum_2])
    return b
