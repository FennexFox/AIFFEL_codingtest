def solution(start_num, end_num):
    answer = []
    
    for num in range(end_num, start_num + 1):
        answer.append(num)
    
    return sorted(answer, reverse = True)