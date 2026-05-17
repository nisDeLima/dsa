class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        # diff[i] represents:
        # "starting at target i, the running cost changes by this amount"
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            if a > b:
                a, b = b, a

            pair_sum = a + b

            # targets reachable with one move:
            # [a + 1, b + limit]
            one_move_left = a + 1
            one_move_right = b + limit

            #
            # Start by assuming:
            # every target costs 2 moves
            #
            diff[2] += 2

            #
            # Reduce cost from 2 -> 1
            # over the one-move interval
            #
            diff[one_move_left] -= 1
            diff[one_move_right + 1] += 1

            #
            # Reduce cost from 1 -> 0
            # at the exact current sum
            #
            diff[pair_sum] -= 1
            diff[pair_sum + 1] += 1

        #
        # Reconstruct actual costs using prefix sum
        #
        answer = float("inf")
        current_cost = 0

        for target in range(2, 2 * limit + 1):
            current_cost += diff[target]
            answer = min(answer, current_cost)

        return answer
