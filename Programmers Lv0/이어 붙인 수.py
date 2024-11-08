def solution(num_list):
    answer = 0
    num1 = num2 = ""
    
    for number in num_list:
        if number % 2 == 1:
            num1 += str(number)
        else:
            num2 += str(number)

    answer = int(num1) + int(num2)
    return answer