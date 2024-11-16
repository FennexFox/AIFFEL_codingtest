def solution(strArr):
    answer = 0
    count = [0 for x in range(30)]
    
    for string in strArr:
        count[len(string)-1] += 1
    
    return sorted(count, reverse = True)[0]