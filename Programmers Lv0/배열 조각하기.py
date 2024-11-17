def solution(arr, query):
    answer = []
    
    for index, integer in enumerate(query):
        if index % 2 == 0:
            arr = arr[:query[index]+1]
        else:
            arr = arr[query[index]:]
    
    return arr