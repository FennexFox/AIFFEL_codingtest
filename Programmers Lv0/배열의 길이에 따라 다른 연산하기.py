def solution(arr, n):
    answer = []
    
    '''
    if와 for가 복잡하게 얽혀있는 게 매우 즐겁지 못하다
    나중에 다시 와서 리팩토링해보자
    '''
    
    if len(arr) % 2 == 1:
        for (index, number) in enumerate(arr):
            if index % 2 == 0:
                answer.append(number + n)
            else:
                answer.append(number)
    elif len(arr) % 2 == 0:
        for (index, number) in enumerate(arr):
            if index % 2 == 1:
                answer.append(number + n)
            else:
                answer.append(number)

    return answer