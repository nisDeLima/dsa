class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        num_jumps = []

        for idx in range(len(dist)):
            d = dist[idx]
            s = speed[idx]
            num_jumps.append(math.ceil(d / s))
        
        num_jumps.sort()
        res = 0
        for i in range(len(num_jumps)):
            if num_jumps[i] > i:
                res += 1
            else:
                break
        
        return res


