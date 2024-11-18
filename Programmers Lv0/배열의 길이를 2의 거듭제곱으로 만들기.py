def solution(arr):
    answer = []
    
    p = 0
    while 2 ** p < len(arr):
        p += 1
    
    temp = [0 for i in range(len(arr), 2 ** p)]
    answer = arr + temp
    
    return answer