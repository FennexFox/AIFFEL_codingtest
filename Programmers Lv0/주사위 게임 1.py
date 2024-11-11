def solution(a, b):
    answer = 0
    
    if (a * b) % 2 == 1:
        answer = a ** 2 + b ** 2
    elif (a + b) % 2 == 1:
        answer = 2 * (a + b)
    else:
        answer = abs(a - b)
    
    return answer