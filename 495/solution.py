class Solution:
    def findPoisonedDuration_rmvd(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        for idx, time in enumerate(timeSeries):
            for t in range(time, time + duration):
                if idx < len(timeSeries) - 1 and t >= timeSeries[idx + 1]:
                    break
                res += 1
        
        return res

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        start, end = timeSeries[0], timeSeries[0] + duration

        for time in timeSeries[1:]:
            res += min(end, time) - start
            start, end = time, time + duration
        
        res += end - start

        return res
