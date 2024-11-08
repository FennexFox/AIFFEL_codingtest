def solution(my_string, alp):
    answer = ''
    
    for letter in my_string:
        if letter == alp:
            answer += letter.upper()
        else:
            answer += letter

    return answer