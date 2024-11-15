def solution(binomial):
    answer = 0
    
    int1, op, int2 = binomial.split()
    
    int1 = int(int1)
    int2 = int(int2)
    
    if op == "+":
        answer = int1 + int2
    elif op == "-":
        answer = int1 - int2
    elif op == "*":
        answer = int1 * int2
    else:
        raise("뭐")
    
    return answer