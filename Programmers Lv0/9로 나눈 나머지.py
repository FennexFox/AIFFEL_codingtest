def solution(number):
    answer = 0
    
    for digit in str(number):
        answer += int(digit)
    
    return answer % 9