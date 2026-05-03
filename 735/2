class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        remaining = []

        for ast in asteroids:
            if ast >= 0:
                remaining.append(ast)
            else:
                while remaining and 0 <= remaining[-1] < abs(ast):
                    remaining.pop()
                if remaining and remaining[-1] == abs(ast):
                    remaining.pop()
                elif(
                    not remaining or
                    remaining[-1] < 0
                ):
                    remaining.append(ast)

        return remaining
