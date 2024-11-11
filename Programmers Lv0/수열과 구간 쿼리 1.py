def solution(arr, queries):

    for query in queries:
        for index in range(query[0], query[1]+1):
            arr[index] += 1
    
    return arr