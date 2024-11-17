def solution(arr):
    
    '''
    너무 우격다짐이라 슬픈 코드
    '''
    
    answer = arr
    rows, columns = len(arr), len(arr[1])

    if rows < columns:
        for i in range(columns - rows):
            answer.append([0 for x in range(columns)])
    elif rows > columns:
        for i in range(len(arr)):
            for j in range(rows - columns):
                answer[i].append(0)
    
    return answer