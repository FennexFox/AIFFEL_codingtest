def solution(board, k):
    answer = 0
    address = []
    
    for i in range(0, min(k+1, len(board))):
        for j in range(0, min(k-i+1, len(board[0]))):
            address.append([i, j])
    
    for cell in address:
        answer += board[cell[0]][cell[1]]
    
    return answer