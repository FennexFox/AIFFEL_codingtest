def solution(arr):
    answer = []
    
    for value in arr:
        to_append = 0
        if (value % 2 == 0) and value >= 50:
            to_append = value/2
        elif (value % 2 == 1) and value < 50:
            to_append = value*2
        else:
            to_append = value
        
        answer.append(to_append)

    return answer