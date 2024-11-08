def solution(arr):
    answer = []
    
    for value in arr:
        for n in range(1, value+1):
            answer.append(value)

    return answer