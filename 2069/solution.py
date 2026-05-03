class Node:
    def __init__(self, direction, length, walk_coord):
        self.direction = direction
        self.length = length
        self.walk_coord = walk_coord
        self.next = None

class Robot:
    def __init__(self, width: int, height: int):
        edges = [
            ("East",  width - 1,  [1, 0]),
            ("North", height - 1, [0, 1]),
            ("West",  width - 1,  [-1, 0]),
            ("South", height - 1, [0, -1]),
        ]
        nodes = [Node(d, l, w) for d, l, w in edges]
        for i in range(len(nodes)):
            nodes[i].next = nodes[(i + 1) % len(nodes)]

        self.curr_edge = nodes[0]
        self.edge_pos = 0
        self.pos = [0, 0]
        self.perimeter = 2 * (width - 1) + 2 * (height - 1)
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        num %= self.perimeter
        while num > 0:
            remaining = self.curr_edge.length - self.edge_pos
            if num <= remaining:
                dx, dy = self.curr_edge.walk_coord
                self.pos[0] += dx * num
                self.pos[1] += dy * num
                self.edge_pos += num
                num = 0
            else:
                dx, dy = self.curr_edge.walk_coord
                self.pos[0] += dx * remaining
                self.pos[1] += dy * remaining
                num -= remaining
                self.curr_edge = self.curr_edge.next
                self.edge_pos = 0

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        if not self.moved:
            return "East"
        if self.edge_pos == 0:
            return self.curr_edge.next.next.next.direction
        return self.curr_edge.direction
