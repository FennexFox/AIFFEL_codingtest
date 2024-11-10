def solution(n):
    answer = []
    
    if n % 2 == 0:
        answer = [4*x ** 2 for x in range(0, int(n/2) + 1)]
    else:
        answer = [2*x + 1 for x in range(0, int((n-1)/2) + 1)]
    
    return sum(answer)