def solution(strArr):
    answer = []
    
    for (index, string) in enumerate(strArr):
        if index % 2 == 1:
            answer.append(string.upper())
        elif index % 2 == 0:
            answer.append(string.lower())
    
    return answer