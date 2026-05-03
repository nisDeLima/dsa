class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        elm_idxs = defaultdict(list)

        def find_pos(arr, elm):
            l, r = 0, len(arr) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == elm:
                    return mid
                if arr[mid] > elm:
                    r = mid - 1
                else:
                    l = mid + 1

        def circular_dist(a, b):
            return min(abs(a - b), n - abs(a - b))

        def find_nearest(curr_idxs, q):
            i = find_pos(curr_idxs, q)
            left = circular_dist(curr_idxs[(i - 1) % len(curr_idxs)], q)
            right = circular_dist(curr_idxs[(i + 1) % len(curr_idxs)], q)
            return min(left, right)

        for idx, num in enumerate(nums):
            elm_idxs[num].append(idx)

        res = []

        for q in queries:
            curr = nums[q]
            curr_idxs = elm_idxs[curr]
            if len(curr_idxs) == 1:
                res.append(-1)
                continue
            else:
                res.append(find_nearest(curr_idxs, q))

        return res
