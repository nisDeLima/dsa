class Solution_rmvd:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        ROWS, COLS = len(coins), len(coins[0])

        @cache
        def get_max(row, col):
            if row == ROWS - 1 and col == COLS - 1:
                mins = [0, 0]
                curr = coins[row][col]
                if curr < 0:
                    mins[0] = curr
                return (curr, mins)
            if row >= ROWS or col >= COLS:
                return (-float("inf"), [0, 0])
            
            curr = coins[row][col]
            min_two = [0, 0]
            if curr < 0:
                min_two.append(curr)
                min_two.sort()

            move_down_val, down_min = get_max(row + 1, col)
            move_right_val, right_min = get_max(row, col + 1)

            if move_down_val + abs(sum(down_min)) > move_right_val + abs(sum(right_min)):
                new_min = down_min + min_two
                new_min.sort()
                return (move_down_val + curr, new_min[:2])
            else:
                new_min = right_min + min_two
                new_min.sort()
                return (move_right_val + curr, new_min[:2])
        
        val, mins = get_max(0, 0)
        return val + abs(sum(mins))

class solution_rmvd1:
    def maximumamount(self, coins: list[list[int]]) -> int:
        rows, cols = len(coins), len(coins[0])

        @cache
        def get_max(row, col, skips=2):
            if row == rows - 1 and col == cols - 1:
                curr = coins[row][col]
                if curr < 0 and skips:
                    return 0
                else:
                    return curr
            if row >= rows or col >= cols:
                return float("-inf")
            
            curr = coins[row][col]

            move_right = get_max(row, col + 1, skips) + curr
            move_down = get_max(row + 1, col, skips) + curr

            skip_right = float("-inf")
            skip_down = float("-inf")

            if curr < 0 and skips:
                skip_right = get_max(row, col + 1, skips - 1)
                skip_down = get_max(row + 1, col, skips - 1)
            
            return max(move_right, move_down, skip_right, skip_down)
        return get_max(0, 0)

class Solution_rmvd2:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        rows, cols = len(coins), len(coins[0])

        @cache
        def get_max(row, col, skips=2):
            if row == rows - 1 and col == cols - 1:
                curr = coins[row][col]
                if curr < 0 and skips:
                    return 0
                else:
                    return curr
            if row >= rows or col >= cols:
                return float("-inf")
            
            curr = coins[row][col]

            move_right = get_max(row, col + 1, skips) + curr
            move_down = get_max(row + 1, col, skips) + curr

            skip = float("-inf")

            if curr < 0 and skips:
                skip = max(get_max(row, col + 1, skips - 1), get_max(row + 1, col, skips - 1))
            
            return max(move_right, move_down, skip)
        return get_max(0, 0)
class Solution_remvd4:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        rows, cols = len(coins), len(coins[0])

        @cache
        def get_max(row, col, skips):
            if row >= rows or col >= cols:
                return float("-inf")

            curr = coins[row][col]

            if row == rows - 1 and col == cols - 1:
                if curr < 0 and skips > 0:
                    return 0
                return curr

            take = curr + max(
                get_max(row + 1, col, skips),
                get_max(row, col + 1, skips)
            )

            if curr < 0 and skips > 0:
                skip = max(
                    get_max(row + 1, col, skips - 1),
                    get_max(row, col + 1, skips - 1)
                )
                return max(take, skip)

            return take

        return get_max(0, 0, 2)
class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        rows, cols = len(coins), len(coins[0])

        dp = [[[float("-inf")] * 3 for _ in range(cols)] for _ in range(rows)]

        for skips in range(3):
            val = coins[rows - 1][cols - 1]
            if val < 0 and skips > 0:
                dp[rows - 1][cols - 1][skips] = 0
            else:
                dp[rows - 1][cols - 1][skips] = val

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row == rows - 1 and col == cols - 1:
                    continue

                curr = coins[row][col]

                for skips in range(3):
                    best = float("-inf")

                    if row + 1 < rows:
                        best = max(best, curr + dp[row + 1][col][skips])

                    if col + 1 < cols:
                        best = max(best, curr + dp[row][col + 1][skips])

                    if curr < 0 and skips > 0:
                        if row + 1 < rows:
                            best = max(best, dp[row + 1][col][skips - 1])

                        if col + 1 < cols:
                            best = max(best, dp[row][col + 1][skips - 1])

                    dp[row][col][skips] = best

        return dp[0][0][2]
