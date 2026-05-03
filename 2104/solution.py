class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        arr = [float("-inf")] + arr + [float("-inf")]
        stack = []  # (index, num)

        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                res = (res + m * left * right)
            stack.append((i, n))
        return res
    def sumSubarrayMax(self, arr: List[int]) -> int:
        res = 0
        arr = [float("inf")] + arr + [float("inf")]
        stack = []  # (index, num)

        for i, n in enumerate(arr):
            while stack and n > stack[-1][1]:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                res = (res + m * left * right)
            stack.append((i, n))
        return res
    def subArrayRanges(self, nums: List[int]) -> int:
        n, answer = len(nums), 0 
        stack = []

        answer -= self.sumSubarrayMins(nums)
        answer += self.sumSubarrayMax(nums)

        return answer
