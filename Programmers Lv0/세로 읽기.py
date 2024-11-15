def solution(my_string, m, c):
    answer = ""
    
    for index, letter in enumerate(my_string):
        if index % m == c - 1:
            answer += letter
    
    return answer