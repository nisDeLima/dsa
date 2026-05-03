class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq_count = Counter(nums)
        sorted_set = sorted(set(nums))
        
        for i in range(len(sorted_set)):
            num_i = sorted_set[i]
            for j in range(i + 1, len(sorted_set)):
                num_j = sorted_set[j]
                if freq_count[num_i] != freq_count[num_j]:
                    return [num_i, num_j]

        return [-1, -1]
