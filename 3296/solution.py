class Solution_rmvd:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        events = [(time, worker, 1) for worker, time in enumerate(workerTimes)]
        heapq.heapify(events)

        while True:
            time, worker, count = heapq.heappop(events)
            mountainHeight -= 1
            if mountainHeight == 0:
                return time
            count += 1
            heapq.heappush(events, (time + workerTimes[worker] * count, worker, count))

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        l, r = 1, min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        def valid(t):
            total = 0
            for w in workerTimes:
                k = int((-1 + math.isqrt(1 + 8 * t // w)) // 2)
                total += k
                if total >= mountainHeight:
                    return True
            return False

        while l <= r:
            mid = l + (r - l) // 2
            if valid(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l
