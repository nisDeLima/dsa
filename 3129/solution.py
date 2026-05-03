class Solution_rmvd:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def get_count(num_zeroes, num_ones, pick_count):
            if num_zeroes == num_ones == 0:
                return 1

            if pick_count == limit:
                if num_zeroes == 0:
                    return 0
                return get_count(num_zeroes - 1, num_ones, -1) % MOD
            if pick_count == -(limit):
                if num_ones == 0:
                    return 0
                return get_count(num_zeroes, num_ones - 1, 1) % MOD

            add_zero = 0
            if num_zeroes:
                new_count = (pick_count - 1) if pick_count < 0 else -1
                add_zero = get_count(num_zeroes - 1, num_ones, new_count)
            add_one = 0
            if num_ones:
                new_count = (pick_count + 1) if pick_count > 0 else 1
                add_one = get_count(num_zeroes, num_ones - 1, new_count)

            return (add_one + add_zero) % MOD

        return get_count(zero, one, 0)

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        for z in range(1, min(zero, limit) + 1):
            dp[z][0][0] = 1
        for o in range(1, min(one, limit) + 1):
            dp[0][o][1] = 1

        for z in range(1, zero + 1):
            for o in range(1, one + 1):
                for k in range(1, min(z, limit) + 1):
                    dp[z][o][0] = (dp[z][o][0] + dp[z - k][o][1]) % MOD

                for k in range(1, min(o, limit) + 1):
                    dp[z][o][1] = (dp[z][o][1] + dp[z][o - k][0]) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
