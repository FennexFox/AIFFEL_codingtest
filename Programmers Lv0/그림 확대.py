def solution(picture, k):
    answer = []
    
    for row in picture:
        temp = ""
        for pixel in row:
            temp += pixel * k
        for i in range(k):
            answer.append(temp)
                
                
                
    
    return answer