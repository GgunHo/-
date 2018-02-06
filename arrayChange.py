def arrayChange(inputArray):
    a = tuple(inputArray)
    for i in range(len(inputArray)-1):
        if inputArray[i] >= inputArray[i+1]:
            inputArray[i+1] = inputArray[i]+1
    
    return sum(inputArray[j]-a[j] for j in range(len(inputArray)))
