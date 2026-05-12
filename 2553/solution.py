class Solution_rmvd:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        def split_num(num):
            res = []
            curr = num

            while curr > 0:
                rest = curr % 10
                curr //= 10
                res.append(rest)
            
            return list(reversed(res))
                

        for num in nums:
            for split in split_num(num):
                res.append(split)
        
        return res

class Solution_r:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            for char in str(num):
                res.append(int(char))
        
        return res

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            while num > 0:
                result.append(num % 10)
                num //= 10
        result.reverse()
        return result
