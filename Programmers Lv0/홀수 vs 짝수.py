def solution(num_list):
    answer = 0
    
    sum1 = sum2 = 0
    
    for (index, num) in enumerate(num_list):
        if index % 2 == 0:
            sum1 += num
        else:
            sum2 += num
    
    answer = max(sum1, sum2)
    
    return answer