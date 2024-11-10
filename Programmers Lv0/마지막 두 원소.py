def solution(num_list):
    answer = num_list
    temp = num_list[-2:]
    
    if temp[1] > temp[0]:
        answer.append(temp[1] - temp[0])
    else:
        answer.append(2 * temp[1])
    
    return answer