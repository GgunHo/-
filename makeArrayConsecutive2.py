def makeArrayConsecutive2(statues):
    a = max(statues)
    b = min(statues)
    c = 0
    for i in range(b,a+1):
        if not i in statues:
            c += 1
            
    return c

#리스트 내에 최소값과 최대값 사이에 비어 있는 수의 개수
