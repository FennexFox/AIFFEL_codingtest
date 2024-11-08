def solution(myString):
    answer = ''
    
    for letter in myString:
        str_append = ""

        if letter == "a":
            str_append = "A"
        elif letter != "A" and letter.lower():
            str_append = letter.lower()
        else:
            str_append = letter
        
        answer += str_append

    return answer