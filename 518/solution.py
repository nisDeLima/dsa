class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev = [0] * (amount + 1)

        for amt in range(amount + 1):
            if amt % coins[0] == 0:
                prev[amt] = 1

        for c_idx in range(1, len(coins)):
            curr = [0] * (amount + 1)
            for amt in range(amount + 1):
                curr[amt] = prev[amt]
                if amt - coins[c_idx] >= 0:
                    curr[amt] += curr[amt - coins[c_idx]]
            prev = curr

        return prev[-1]
