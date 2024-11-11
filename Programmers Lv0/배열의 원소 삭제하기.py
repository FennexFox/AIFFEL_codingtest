def solution(arr, delete_list):
    answer = []
    
    for int in arr:
        if not int in delete_list:
            answer.append(int)
    
    return answer