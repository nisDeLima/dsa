class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if target:
            ops = target[0]
            for idx in range(1, len(target)):
                ops += max(target[idx] - target[idx - 1], 0)
            return ops
        return 0
