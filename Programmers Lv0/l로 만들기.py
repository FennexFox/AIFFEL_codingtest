def solution(myString):
    answer = ''
    
    for letter in myString:
        if ord(letter) < ord('l'):
            answer += 'l'
        else:
            answer += letter

    return answer