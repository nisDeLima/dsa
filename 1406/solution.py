class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        target = sum(stoneValue) / 2

        @cache
        def dfs(alice_turn, stone):
            if stone >= len(stoneValue):
                return 0

            points = float("-inf")
            if alice_turn:
                for i in range(1, 4):  # Take 1, 2, or 3 stones
                    if stone + i <= len(stoneValue):
                        points = max(
                            points, 
                            sum(stoneValue[stone:stone+i]) + dfs(not alice_turn, stone + i)
                        )
            else:
                points = float("inf")
                for i in range(1, 4):  # Take 1, 2, or 3 stones
                    if stone + i <= len(stoneValue):
                        points = min(
                            points, 
                            dfs(not alice_turn, stone + i)
                        )

            return points

        alice_points = dfs(True, 0)
        if alice_points > target:
            return "Alice"
        elif alice_points < target:
            return "Bob"

        return "Tie"
