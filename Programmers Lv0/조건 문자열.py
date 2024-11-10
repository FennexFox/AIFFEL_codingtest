def solution(ineq, eq, n, m):
    answer = 0
    
    if eq == "=" and n == m:
        answer = 1
    elif ineq == ">" and n > m:
        answer = 1
    elif ineq == "<" and n < m:
        answer = 1
    
    return answer