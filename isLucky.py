def isLucky(n):
    
    list_1 = []
    a = len(str(n))/2
    f_sum = 0
    s_sum = 0
    
    if len(str(n)) % 2 == 0 :
        for i in range(len(str(n))):
            list_1.append(int(str(n)[i]))
        for j in range(int(a)):
            f_sum += list_1[j]
            s_sum += list_1[-(j+1)]
        return f_sum == s_sum 
            

'''숫자 중 반을 나눠 앞자리의 합과 뒷자리의 합이 같으면 true 다른면 false
    우선 숫자의 길이가 짝수인지 확인
    숫자를 리스트화 시켜서 반을 나눠 앞, 뒤 합을 따로 저장'''
