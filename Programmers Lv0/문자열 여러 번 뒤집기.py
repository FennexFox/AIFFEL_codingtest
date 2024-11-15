def solution(my_string, queries):
    answer = my_string
    
    for query in queries:
        answer = answer[:query[0]] + answer[query[0]:query[1]+1][::-1] + answer[query[1]+1:]
    
    return answer