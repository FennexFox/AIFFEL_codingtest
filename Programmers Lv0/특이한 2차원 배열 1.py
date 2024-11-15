def solution(n):
    answer = [[0 for x in range(n)] for y in range(n)]
    
    for i in range(n):
        answer[i][i] = 1
    
    return answer