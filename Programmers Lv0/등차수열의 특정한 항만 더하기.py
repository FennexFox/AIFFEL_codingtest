def solution(a, d, included):
    answer = 0
    
    for i in range(0, len(included)):
        if included[i]:
            answer += a + d * i
        
    return answer