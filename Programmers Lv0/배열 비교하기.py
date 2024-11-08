from functools import reduce

def solution(arr1, arr2):
    answer = 0
    
    if len(arr1) == len(arr2):
        size1 = reduce(lambda x, y: x + y, arr1)
        size2 = reduce(lambda x, y: x + y, arr2)
    else:
        size1 = len(arr1)
        size2 = len(arr2)
    
    if size1 > size2:
        answer = 1
    elif size1 < size2:
        answer = -1

    return answer