def almostIncreasingSequence(sequence):
    
    a = 0
    b = 0
    
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]  :
            a += 1
            
    for j in range(len(sequence)-2):
            if sequence[j] >= sequence[j+2]:
                b += 1    
            
    return (a <= 1 | b<=1)   
        
'''리스트내에서 숫자 하나를 제외하면 증가수열이 되는가?
    처음 for문에서 바로 옆자리와 비교하여 작은 수이면 a 에 +1
    다음 for문에서 옆옆자리와 비교하여 작은 수 이면 b에 +1
    최종적으로 a혹은 b가 1 이하인가'''
