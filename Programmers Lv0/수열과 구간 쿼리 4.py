def solution(arr, queries):

    for i in range(0, len(arr)):
        for query in queries:
            if query[0] <= i and i <= query[1] and i % query[2] == 0:
                arr[i] += 1

    return arr