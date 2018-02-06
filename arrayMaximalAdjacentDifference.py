def arrayMaximalAdjacentDifference(inputArray):
    a= []
    for i in range(len(inputArray)-1):
        a += [abs(inputArray[i]-inputArray[i+1])]
    return max(a)     
