class Solution:
    def countQuadruplets_removed(self, nums: List[int]) -> int:
        num_idx = defaultdict(list)
        for i, num in enumerate(nums):
            num_idx[num].append(i)

        count = 0 
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for z in range(j + 1, len(nums)):
                    curr_sum = nums[i] + nums[j] + nums[z]
                    if curr_sum in num_idx:
                        for cand in num_idx[curr_sum]:
                            if cand > z:
                                count += 1
        return count
        
    def countQuadruplets(self, nums: List[int]) -> int:
        num_idx = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                num_i = nums[i]
                num_j = nums[j]
                num_idx[num_i + num_j].append(j)

        count = 0 
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                num_i = nums[i]
                num_j = nums[j]

                if (num_j - num_i) in num_idx:
                    for cand in num_idx[(num_j - num_i)]:
                        if cand < i:
                            count += 1

        return count
        
