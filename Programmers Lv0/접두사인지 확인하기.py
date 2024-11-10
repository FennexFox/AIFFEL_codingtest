def solution(my_string, is_prefix):
    answer = 1
    
    if len(my_string) < len(is_prefix):
        answer = 0
    else:
        for index in range(0, len(is_prefix)):
            if my_string[:index] != is_prefix[:index]:
                answer = 0
                break

    return answer