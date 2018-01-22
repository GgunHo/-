def commonCharacterCount(s1, s2):
    
    def listst(x):
        y = []
        for i in range(len(x)):
            y.append(x[i])
        return y
    
    s1_1=listst(s1)
    s2_1=listst(s2)

    a = []
    b = min(len(s1),len(s2))


    for i in range(b):
        if s1_1[i] in s2_1:
            a.append(s1_1[i])
            s2_1.remove(s1_1[i])
    return len(a)

''' s1,s2의 공통된 문자가 몇개인지 추출
    listst라는 함수를 정의 : 문자열을 리스트화 시키기
    s1과 s2를 리스트화
    가장 짧은 숫자만큼 for문 실행하여 S2에 s1이 있는지 확인하여
    있다면 리스트에 추가하고 s2에서 문자 삭제'''

