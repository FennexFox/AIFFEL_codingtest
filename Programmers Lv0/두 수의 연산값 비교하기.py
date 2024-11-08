def solution(a, b):
    answer = 0
    
    num1 = int(str(a) + str(b))
    num2 = 2 * a * b

    '''
    if문을 여기 쓰는 의미를 모르겠지만 문제에서 요구하니 작성함
    call by address와 call by value의 차이일까?
    파이썬에도 그게 있는지 모르겠다
    '''

    if num1 == num2:
        answer = num1
    else:
        answer = max(num1, num2)

    return answer