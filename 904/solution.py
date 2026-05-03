class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0

        l = 0
        types_count = defaultdict(int)
        ans = 1

        for r in range(len(fruits)):
            types_count[fruits[r]] += 1
            while len(types_count) > 2:
                fruit_to_remove = fruits[l]
                types_count[fruit_to_remove] -= 1
                l += 1
                if types_count[fruit_to_remove] == 0:
                    del types_count[fruit_to_remove]
            ans = max(ans, r - l + 1)

        return ans
