def solution(my_string, indices):
    answer = [char for char in my_string]
    
    for index in indices:
        answer[index] = 0
    
    while 0 in answer:
        answer.remove(0)

    return "".join(answer)