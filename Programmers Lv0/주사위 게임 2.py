def solution(a, b, c):
    answer = a + b + c
    
    '''
    사람이 보기에 쉽거나 기계가 보기에 쉬워야 하는데
    이건 사람이 보기에도 기계가 보기에도 짜증나는 것 같음
    '''
    
    if a == b or b == c or c == a:
        answer *= (a ** 2) + (b ** 2) + (c ** 2)
        if a == b and b == c:
            answer *= (a ** 3) + (b ** 3) + (c ** 3)
    
    return answer