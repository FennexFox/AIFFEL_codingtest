def solution(arr, flag):
    answer = []
    
    for integer, boolean in zip(arr, flag):
        if boolean:
            answer = answer + [integer for x in range(integer * 2)]
        else:
            answer = answer[:-integer]
    
    return answer