class Solution_rmvd:
    def longestRepeatingSubstring(self, s: str) -> int:
        counter = defaultdict(int)

        for i in range(len(s)):
            for j in range(i, len(s)):
                counter[s[i:j + 1]] += 1
        
        res = 0

        for key, val in counter.items():
            if val > 1:
                res = max(res, len(key))
        
        return res
    
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return 0

        left = 0
        right = len(s) - 1

        res = 0

        while left <= right:
            mid = left + ((right - left) // 2)

            has_repeated = self.has_repeated(mid, s)
            if has_repeated:
                left = mid + 1
                res = mid
            else:
                right = mid - 1

        return res

    def has_repeated(self, search_len, s):
        seen = set()
        for i in range(0, len(s) - search_len + 1):
            sub_str = s[i: i + search_len]
            if sub_str in seen:
                return True

            seen.add(sub_str)

        return False 
