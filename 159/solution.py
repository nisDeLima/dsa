class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        ans = 0
        counter = defaultdict(int)

        for r in range(len(s)):
            counter[s[r]] += 1
            while len(counter) > 2:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
            ans = max(ans, r - l + 1)

        return ans
