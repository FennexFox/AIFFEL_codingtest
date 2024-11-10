def solution(n, control):
    answer = n
    
    for input in control:
        if input == "w":
            answer += 1
        elif input == "s":
            answer -= 1
        elif input == "d":
            answer += 10
        elif input == "a":
            answer -= 10
    
    return answer