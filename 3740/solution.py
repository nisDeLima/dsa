class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        val_idxs = defaultdict(list)

        for idx, num in enumerate(nums):
            val_idxs[num].append(idx)
        
        res = float("inf")

        def set_res(idxs):
            curr = float("inf")

            if len(idxs) < 3:
                return curr

            for r in range(2, len(idxs)):
                i = idxs[r - 2]
                j = idxs[r - 1]
                k = idxs[r]

                curr = min(curr, (
                    abs(i - j) + abs(j - k) + abs(k - i)
                ))
            
            return curr
            


        for val in val_idxs.values():
            res = min(set_res(val), res)

        return res if res != float("inf") else -1
