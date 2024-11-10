def solution(n, k):
    answer = []
    
    for number in range(1, n//k+1):
        answer.append(number*k)
    
    return answer