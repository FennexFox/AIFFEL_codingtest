from functools import reduce

def solution(num_list):
    answer = 0
    
    num1 = reduce(lambda x, y: x*y, num_list)
    num2 = reduce(lambda x, y: x+y, num_list)
    
    if num1 < num2 ** 2:
        answer = 1
    
    return answer