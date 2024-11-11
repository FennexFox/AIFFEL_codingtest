def solution(arr, k):
    answer = []

    for integer in arr:
        if k % 2 == 0:
            answer.append(integer + k)
        else:
            answer.append(integer * k)

    return answer