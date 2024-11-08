def solution(str1, str2):
    answer = ''
    
    for i in range(0, len(str1)+1):
        answer += str1[i:i+1] + str2[i:i+1]
    
    return answer