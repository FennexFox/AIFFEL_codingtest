def solution(my_string):
    answer = []
    
    for index in range(1, len(my_string)+1):
        answer.append(my_string[-index:])
    
    return sorted(answer)