def solution(num_list, n):
    answer = []
    
    for (index, num) in enumerate(num_list):
        if index % n == 0:
            answer.append(num)
    
    return answer