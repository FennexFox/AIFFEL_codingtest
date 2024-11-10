def solution(code):
    answer = ''
    mode = 0
    
    for (idx, letter) in enumerate(code):
        if mode == 0:
            if letter == "1":
                mode = 1
            elif idx % 2 == 0:
                answer += letter
        elif mode == 1:
            if letter == "1":
                mode = 0
            elif idx % 2 == 1:
                answer += letter
    
    if not answer:
        answer = "EMPTY"
    
    return answer