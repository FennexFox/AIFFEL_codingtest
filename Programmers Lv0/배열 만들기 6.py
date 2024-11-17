def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if len(stk) < 1:
            stk = [arr[i]]
        elif stk[-1] == arr[i]:
            stk.pop()
        elif stk[-1] != arr[i]:
            stk.append(arr[i])
        i += 1
    
    if len(stk) < 1:
        stk = [-1]
        
    return stk