def adjacentElementsProduct(inputArray):
    result = inputArray[0]*inputArray[1] # 초기값 설정
    
    for i in range(len(inputArray)-1):
        if result >= inputArray[i]*inputArray[i+1] :
            result = result
        else :
            result = inputArray[i]*inputArray[i+1]
    return result

