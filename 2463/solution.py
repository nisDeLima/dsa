class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        @cache
        def dp(f, r):
            if r == len(robot):
                return 0

            if f == len(factory):
                return float("inf")

            pos, limit = factory[f]

            # option 1: skip this factory
            best = dp(f + 1, r)

            # option 2: assign 1..limit robots here
            cost = 0
            for k in range(limit):
                if r + k >= len(robot):
                    break

                cost += abs(robot[r + k] - pos)
                best = min(best, cost + dp(f + 1, r + k + 1))

            return best

        return dp(0, 0)
