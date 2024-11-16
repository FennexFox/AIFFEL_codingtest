def solution(q, r, code):
    answer = ''
    
    for index, letter in enumerate(code):
        if index % q == r:
            answer += letter
    
    return answer