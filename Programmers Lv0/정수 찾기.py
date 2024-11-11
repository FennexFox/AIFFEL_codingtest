def solution(num_list, n):
    answer = (lambda x, y: 1 if y in x else 0)(num_list, n)
    return answer