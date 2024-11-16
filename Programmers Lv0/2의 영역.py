def solution(arr):
    answer = []
    temp = []
    
    for index, integer in enumerate(arr):
        if integer == 2:
            temp.append(index)

    if len(temp) > 0:
        answer = arr[temp[0]:temp[len(temp)-1]+1]
    else:
        answer = [-1]
    
    return answer