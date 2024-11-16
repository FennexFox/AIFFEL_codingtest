def solution(myString, pat):
    answer = 0
    
    while pat in myString:
        answer += 1
        myString = myString[myString.find(pat)+1:]
    
    return answer