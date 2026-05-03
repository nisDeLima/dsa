class Solution:
    def minOperations(self, s: str) -> int:
        start_one = 0
        start_zero = 0

        for idx, char in enumerate(s):
            if idx % 2 == 0:
                if char == "1":
                    start_zero += 1
                if char == "0":
                    start_one += 1
            else:
                if char == "1":
                    start_one += 1
                if char == "0":
                    start_zero += 1
        
        return min(start_one, start_zero)
