def solution(myStr):
    answer = []
    temp = 0
    temp_list = ["a", "b", "c"]
    
    for index, char in enumerate(myStr):
        if char in temp_list:
            if temp != index:
                answer.append(myStr[temp:index])
            temp = index + 1
        if index + 1 == len(myStr):
            answer.append(myStr[temp:index + 1])
    
    if not answer[0]:
        answer = ["EMPTY"]

    return answer