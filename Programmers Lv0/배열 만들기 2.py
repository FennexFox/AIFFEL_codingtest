def solution(l, r):
    answer = []
    
    for integer in range(l, r+1):
        answer.append(integer)
        for digit in str(integer):
            if digit != "5" and digit != "0":
                answer.pop()
                break
                
    
    if len(answer) == 0:
        answer = [-1]
    
    return answer