def allLongestStrings(inputArray):
        a = []
        b = []
        for i in range(len(inputArray)):
                a.append(len(inputArray[i]))
                      
        for j in range(len(inputArray)):
                if len(inputArray[j]) == max(a):
                        b.append(inputArray[j])
        return b
            

''' 리스트 중 가장 길이 가 긴 문자 추출
        처음 for문에서 a라는 리스트에 inputArray의 리스트내 문자의 길이를 입력 
        다음 for문에서 a의 최대값과 inputArray의 리스트내 문자의 길이가 같다면
        b라는 리스트에 추가 '''
