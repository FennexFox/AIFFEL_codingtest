def solution(arr, k):
    answer = []
    
    for integer in arr:
        if not (integer in answer) and len(answer) < k:
            answer.append(integer)

    while len(answer) < k:
        answer.append(-1)
    
    return answer