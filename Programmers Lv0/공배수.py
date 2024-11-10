def solution(number, n, m):
    answer = 0
    
    '''
    이게 일반적인 if and 구문보다 더 빠를까?
    '''
    
    if (number % n) + (number % m) == 0:
        answer = 1
    
    return answer