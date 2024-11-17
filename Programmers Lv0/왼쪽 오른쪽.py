def solution(str_list):
    
    '''
    사람을 굉장히 불행하게 만드는 코드
    if문을 좀 정리해보자
    '''
    
    answer = []
    l_index = r_index = -1
    
    try:
        l_index = str_list.index('l')
    except:
        pass
    
    try:
        r_index = str_list.index('r')
    except:
        pass
    
    if not (l_index == -1 or r_index == -1):
        if l_index < r_index:
            answer = str_list[:l_index]
        elif l_index > r_index:
            answer = str_list[r_index + 1:]
    elif l_index * r_index != 1:
        r_index = max(r_index+1, 0)
        if l_index == -1:
            l_index = len(str_list)
        
        answer = str_list[r_index:l_index]

    return answer