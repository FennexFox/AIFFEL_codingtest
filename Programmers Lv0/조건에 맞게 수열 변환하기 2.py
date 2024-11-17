def solution(arr):
    prev_step = arr
    next_step = stepper(arr)
    answer = 0
    
    while next_step != prev_step:
        prev_step = next_step
        next_step = stepper(next_step)
        answer += 1
    
    return answer

def stepper(arr):
    next_step = ([x / 2 if x >= 50 and x % 2 == 0 else
               2 * x + 1 if x < 50 and x % 2 == 1 else
               x for x in arr])

    return next_step