def solution(myString, pat):
    answer = 0
    test_string = ""
    
    for letter in myString:
        if letter == "A":
            test_string += "B"
        elif letter == "B":
            test_string += "A"
        else:
            test_string += letter
    
    if pat in test_string:
        answer = 1

    return answer