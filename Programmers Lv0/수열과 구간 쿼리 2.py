def solution(arr, queries):
    answer = []
    
    for query in queries:
        temp1 = []
        temp2 = arr[query[0]:query[1]+1]

        for integer in temp2:
            if integer > query[2]:
                temp1.append(integer)
        
        if len(temp1) > 0:
            answer.append(sorted(temp1)[0])
        else:
            answer.append(-1)

    return answer