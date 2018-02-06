def palindromeRearranging(inputString):
    a = 0 #중복된 숫자가 홀수 개인경우 1추가
    b = set(inputString) #중복제거
    for i in b:
        k = inputString.count(i)
        if k%2!=0:
            a += 1 
    return a <= 1
