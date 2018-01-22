def sortByHeight(a):
        for i in range(len(a)-1):
            if a[i] == -1 :
                pass
            else:
                for j in range(i+1, len(a)):
                    if a[j] == -1:
                        pass
                    else:
                        if a[i] > a[j]:
                                a[i], a[j] = a[j], a[i]        
        return a
            

'''-1은 고정시키고 나머지 숫자를 정렬시키기
        i를 고정시키고 -1을 제외한 나머지 숫자(j)와 비교하여 정렬
        j가 끝까지 가면 i를 증가시켜 리스트가 정렬이 될 수 있도록 함'''
