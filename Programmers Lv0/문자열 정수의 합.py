from functools import reduce

def solution(num_str):
    answer = reduce(lambda x, y: int(x) + int(y), num_str)
    return answer