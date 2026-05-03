class Solution:
    def maxScore(self, s: str) -> int:
        ones_right = s.count("1")
        max_val = 0
        left_score = 0

        # stop before last char
        for i in range(len(s) - 1):
            if s[i] == "0":
                left_score += 1
            else:
                ones_right -= 1

            max_val = max(max_val, left_score + ones_right)

        return max_val
