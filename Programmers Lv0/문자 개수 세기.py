def solution(my_string):
    answer = []
    
    for index in range(ord("A"), ord("Z")+1):
        answer.append(my_string.count(chr(index)))

    for index in range(ord("a"), ord("z")+1):
        answer.append(my_string.count(chr(index)))
    
    return answer