def solution(my_string):
    
    '''
    가능하면 정규식과 string 라이브러리를 써서 다시 해보자
    '''
    
    answer = []
    temp_string = my_string.split(" ")
    
    for string in temp_string:
        if string != "":
            answer.append(string)

    return answer