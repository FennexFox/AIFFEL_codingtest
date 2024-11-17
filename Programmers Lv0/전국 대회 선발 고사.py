def solution(rank, attendance):
    answer = i = 0
    temp = {}
    
    for position, is_attending in zip(rank, attendance):
        if is_attending:
            temp.setdefault(position, i)
        i += 1
    
    temp = sorted(temp.items())
    answer = 10000 * temp[0][1] + 100 * temp[1][1] + temp[2][1]
    
    return answer