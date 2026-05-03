class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        self.walk_coord = [0, 0]

class Compass:
    def __init__(self):
        self.R = Node("R")
        self.R.walk_coord = [1, 0]
        self.U = Node("U")
        self.U.walk_coord = [0, 1]
        self.L = Node("L")
        self.L.walk_coord = [-1, 0]
        self.D = Node("D")
        self.D.walk_coord = [0, -1]

        self.U.next, self.U.prev = self.R, self.L
        self.R.next, self.R.prev = self.D, self.U
        self.L.next, self.L.prev = self.U, self.D
        self.D.next, self.D.prev = self.L, self.R

        self.curr_dir = self.U
        self.curr_pos = [0, 0]

    def peek(self):
        row, col = self.curr_pos
        return [row + self.curr_dir.walk_coord[0], col + self.curr_dir.walk_coord[1]]
    
    def walk(self):
        row, col = self.curr_pos 
        self.curr_pos = [row + self.curr_dir.walk_coord[0], col + self.curr_dir.walk_coord[1]]
        return self.curr_pos

    def turn(self, command):
        if command == -1:
            self.curr_dir = self.curr_dir.next
        elif command == -2:
            self.curr_dir = self.curr_dir.prev

class Solution_rmvd:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def calc_dist(pos):
            row, col = pos
            return row ** 2 + col ** 2
        
        compass = Compass()
        obstacle_set = set(map(tuple, obstacles))
        res = 0

        for idx, command in enumerate(commands):
            if command in [-1, -2]:
                compass.turn(command)
            else:
                for step in range(command):
                    if tuple(compass.peek()) in obstacle_set:
                        break
                    next_pos = compass.walk()
                    res = max(res, calc_dist(next_pos))
        return res
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W
        d = 0
        x = y = res = 0
        obstacle_set = set(map(tuple, obstacles))

        for command in commands:
            if command == -1:
                d = (d + 1) % 4
            elif command == -2:
                d = (d - 1) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(command):
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    x += dx
                    y += dy
                    res = max(res, x * x + y * y)
        return res
