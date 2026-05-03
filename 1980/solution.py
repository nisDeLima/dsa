class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        L = len(nums)
        nums_set = set(nums)
        self.res = ""

        def generate(i, num):
            if i == L:
                if num not in nums_set:
                    self.res = num
                    return -1
                return 1

            if generate(i + 1, num + "1") == -1 or generate(i + 1, num + "0") == -1:
                return 0
        generate(0, "")
        return self.res

### Now the smart way
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        max_num = 0
        num_set = set()
        for idx, num in enumerate(nums):
            num_set.add(int(num, 2))
            max_num += 2 ** idx

        for i in range(max_num + 1):
            if i not in num_set:
                return format(i, f'0{n}b')

### Now the smarter way
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        res = []

        for i in range(n):
            res.append('1' if nums[i][i]=='0' else '0')

        return ''.join(res)
