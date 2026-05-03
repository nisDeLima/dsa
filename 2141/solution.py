class Solution:
    def maxRunTime_timedout(self, n: int, batteries: List[int]) -> int:
        res = 0
        # max heap via negation
        heap = [-b for b in batteries]
        heapq.heapify(heap)

        while len(heap) >= n:
            res += 1
            temp = []
            for _ in range(n):
                if not heap:
                    return res
                curr = heapq.heappop(heap)
                curr += 1  # add 1 because curr is negative
                if curr < 0:  # still has charge
                    temp.append(curr)

            for item in temp:
                heapq.heappush(heap, item)

        return res
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def verify(time):
            avail = 0
            for batt in batteries:
                avail += min(time, batt)
            return avail // n >= time
        
        l, r = 1, sum(batteries) // n

        while l < r:
            mid = l + (r - l + 1) // 2
            if verify(mid):
                l = mid
            else:
                r = mid - 1
        return l
