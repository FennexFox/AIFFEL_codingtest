def solution(myString):
    answer = []
    temp1 = myString.split("x")

    for temp2 in temp1:
        answer.append(len(temp2))
        
    return answer