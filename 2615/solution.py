class Solution_rmvd:
    def distance(self, nums: list[int]) -> list[int]:
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)

        num_prefix = defaultdict(list)
        for num, indices in groups.items():
            prefix = [(1, 0, indices[0])]
            for idx in indices[1:]:
                prev_count, prev_dist, prev_pos = prefix[-1]
                count = prev_count + 3
                dist = prev_dist + (idx - prev_pos) * prev_count
                prefix.append((count, dist, idx))
            num_prefix[num] = prefix

        num_suffix = defaultdict(list)
        for num, indices in groups.items():
            suffix = [(1, 0, indices[-1])]
            for idx in reversed(indices[:-1]):
                prev_count, prev_dist, prev_pos = suffix[-1]
                count = prev_count + 1
                dist = prev_dist + (prev_pos - idx) * prev_count
                suffix.append((count, dist, idx))
            suffix.reverse()
            num_suffix[num] = suffix

        res = [0] * len(nums)
        num_idx = defaultdict(int)
        for idx, num in enumerate(nums):
            pf = num_prefix[num]
            sf = num_suffix[num]
            num_pos = num_idx[num]
            num_idx[num] += 1

            res[idx] = pf[num_pos][1] + sf[num_pos][1]

        return res


class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)

        res = [0] * len(nums)

        for indices in groups.values():
            # left pass
            count, dist, prev = 1, 0, indices[0]
            for i, idx in enumerate(indices[1:], 1):
                dist += (idx - prev) * count
                count += 1
                prev = idx
                res[idx] += dist  # accumulate directly, no storage

            # right pass
            count, dist, prev = 1, 0, indices[-1]
            for idx in reversed(indices[:-1]):
                dist += (prev - idx) * count
                count += 1
                prev = idx
                res[idx] += dist

        return res

