def solution(numLog):
    answer = ''
    num_prev = num_delta = 0
    
    for num in numLog:
        num_delta = num - num_prev
        if num_delta == 1:
            answer += "w"
        elif num_delta == -1:
            answer += "s"
        elif num_delta == 10:
            answer += "d"
        elif num_delta == -10:
            answer += "a"
        
        num_prev = num
    
    return answer