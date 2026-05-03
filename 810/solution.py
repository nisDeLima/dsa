class Solution_rmvd:
    def xorGame(self, nums: List[int]) -> bool:
        def is_xor(removed):
            result = 0
            for idx, num in enumerate(nums):
                if idx not in removed:
                    result ^= num
            return result == 0
    
        @cache
        def dfs(i, removed):
            if is_xor(removed):
                return i % 2 == 0 
            tests = [] 
            for j in range(len(nums)):
                if j not in removed:
                    tests.append(dfs(i + 1, removed | {j}))
            if i % 2 == 0: 
                return any(tests)
            else: 
                return all(tests)

        return dfs(0, frozenset())
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        xor = 0
        for num in nums:
            xor ^= num
        return xor == 0 or len(nums) % 2 == 0
