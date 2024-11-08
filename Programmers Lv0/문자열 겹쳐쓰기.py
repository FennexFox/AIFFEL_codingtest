def solution(my_string, overwrite_string, s):
    answer = ''
    t = s + len(overwrite_string)
    
    answer = my_string[:s] + overwrite_string + my_string[t:]
    return answer