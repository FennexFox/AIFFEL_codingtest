def solution(n):
    answer = IntegerSpiral(n)
    
    return answer.writer()

'''
아주 불행한 코드

'''

class IntegerSpiral:
    def __init__(self, n:int):
        self.spiral = [[0 for x in range(n)]for y in range(n)]
        self.spiral_len = n
        self.position = [0, 0]
        self.integer = 1
        self.direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.direction_step = 0
    
    def mover(self):
        direction = self.direction[self.direction_step]
        coordinate = []
        
        for position, direction in zip(self.position, direction):
            coordinate.append(max(min(position + direction, self.spiral_len-1), 0))

        if self.spiral[coordinate[0]][coordinate[1]] == 0:
            self.position = coordinate
        else:
            self.direction_step = (self.direction_step + 1) % 4
            self.mover()
        
    def writer(self):
        while self.integer < self.spiral_len ** 2:
            self.spiral[self.position[0]][self.position[1]] = self.integer
            self.integer += 1
            self.mover()
        
        self.spiral[self.position[0]][self.position[1]] = self.integer
        
        return self.spiral