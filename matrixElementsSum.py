def matrixElementsSum(matrix):
    sum = 0 
    
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i+1][j] = 0
            
            
    for k in range(len(matrix)):
        for l in range(len(matrix[k])):
            sum += matrix[k][l]           

    return sum        
            
            
''' 행렬에서 숫자 0 밑에자리는 모두 0으로 변환
    핼렬에 있는 모든 값 더하기'''
