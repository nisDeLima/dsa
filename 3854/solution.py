class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0, 0]
        start_even_change = []
        start_odd_change = []

        for idx, num in enumerate(nums):
            if (idx + 1) % 2 == 0:
                if num % 2 == 0:
                    start_even_change.append(idx)
                else:
                    start_odd_change.append(idx)
            else:
                if num % 2 != 0:
                    start_even_change.append(idx)
                else:
                    start_odd_change.append(idx)

        se = set(start_even_change)
        so = set(start_odd_change)

        mn = min(nums)
        mx = max(nums)

        def apply_changes(changes: set) -> tuple[int, int]:
            keep_min = keep_max = False

            for i, x in enumerate(nums):
                if i not in changes:
                    # this element stays as-is
                    if x == mn:
                        keep_min = True
                    if x == mx:
                        keep_max = True

            new_min = mn if keep_min else mn + 1
            new_max = mx if keep_max else mx - 1

            return len(changes), max(new_max - new_min, 1)

        if len(se) == len(so):
            return list(min(apply_changes(se), apply_changes(so)))

        chosen = se if len(se) < len(so) else so
        return list(apply_changes(chosen))
