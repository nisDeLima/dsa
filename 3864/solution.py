class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        @cache
        def calc_value(bin_s):
            ones = Counter(bin_s)["1"]
            if ones == 0:
                return flatCost
            
            return len(bin_s) * ones * encCost

        @cache
        def get_min(curr):
            len_curr = len(curr)
            half = len_curr // 2
            if len_curr % 2 != 0:
                return calc_value(curr)
            
            stop_now = calc_value(curr)
            split = get_min(curr[:half]) + get_min(curr[half:])

            return min(stop_now, split)

        return get_min(s)
