class Solution:
    def minimumMountainRemovals_v1_recursive_dp(self, nums: List[int]) -> int:
        """
        Version 1: Recursive DP with Memoization - The Memory Hog
        
        Approach: Classic recursive DP to find Longest Increasing Subsequence (LIS)
        and Longest Decreasing Subsequence (LDS) from each position.
        
        Time Complexity: O(N²) - We check every pair of indices
        Space Complexity: O(N²) - FATAL FLAW! Cache stores every (index, prev) pair
        
        Why it fails: The @cache decorator stores ALL possible combinations of
        (i, prev), resulting in N * N cache entries. For large inputs, this
        causes Out of Memory errors.
        
        Educational value: Shows how naive memoization can backfire spectacularly.
        """
        N = len(nums)

        @cache
        def lis_from_position(i, prev):
            # Base case: reached end of array
            if i == N:
                return 0
            
            # Option 1: Include current element if it forms increasing sequence
            take = 0  # Better than float("-inf") for clarity
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + lis_from_position(i + 1, i)
            
            # Option 2: Skip current element
            skip = lis_from_position(i + 1, prev)

            return max(take, skip)
        
        # Calculate LIS from each starting position (going left to right)
        lis_lengths = []
        for i in range(N):
            lis_lengths.append(lis_from_position(i, -1))

        # Clear cache before redefining function (crucial but hacky)
        lis_from_position.cache_clear()
        
        # Redefine for right-to-left traversal (this is terrible practice)
        @cache
        def lds_from_position(i, prev):
            # Base case: reached beginning of array
            if i == -1:
                return 0
            
            # Option 1: Include current element if it forms decreasing sequence
            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + lds_from_position(i - 1, i)
            
            # Option 2: Skip current element
            skip = lds_from_position(i - 1, prev)

            return max(take, skip)
        
        # Calculate LDS from each starting position (going right to left)
        lds_lengths = []
        for i in range(N):
            lds_lengths.append(lds_from_position(i, -1))

        # Find the longest valid mountain
        # Mountain requires: increasing part + peak + decreasing part
        longest_mountain = 0
        for i in range(N):
            # Valid mountain peak must have elements on both sides
            if lis_lengths[i] > 1 and lds_lengths[i] > 1:
                # -1 because peak is counted in both sequences
                mountain_length = lis_lengths[i] + lds_lengths[i] - 1
                longest_mountain = max(longest_mountain, mountain_length)
        
        # Return minimum removals = total elements - longest mountain
        return N - longest_mountain

    def minimumMountainRemovals_v2_iterative_dp(self, nums: List[int]) -> int:
        """
        Version 2: Classic Iterative Dynamic Programming
        
        Approach: Build up LIS/LDS lengths using bottom-up DP.
        For each position, check all previous positions.
        
        Time Complexity: O(N²) - Double nested loops
        Space Complexity: O(N) - Only store lengths array
        
        Why it's better: No recursion overhead, no massive cache.
        Why optimize further: O(N²) is still slow for large inputs.
        
        This is the "textbook" solution - clean, correct, but not optimal.
        """
        N = len(nums)

        # lis_ending[i] = length of LIS ending at index i
        lis_ending = [1] * N  # Every element is a subsequence of length 1
        
        # Build LIS using classic DP approach
        for i in range(N):
            for j in range(i):
                # If we can extend the LIS ending at j by including nums[i]
                if nums[j] < nums[i]:
                    lis_ending[i] = max(lis_ending[i], lis_ending[j] + 1)

        # lds_starting[i] = length of LDS starting at index i
        lds_starting = [1] * N
        
        # Build LDS by iterating backwards
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                # If we can extend the LDS starting at j by including nums[i]
                if nums[i] > nums[j]:
                    lds_starting[i] = max(lds_starting[i], lds_starting[j] + 1)

        # Find the longest valid mountain
        longest_mountain = 0
        for i in range(1, N - 1):  # Peak can't be at array boundaries
            # Valid mountain needs both sides to have length > 1
            if lis_ending[i] > 1 and lds_starting[i] > 1:
                mountain_length = lis_ending[i] + lds_starting[i] - 1
                longest_mountain = max(longest_mountain, mountain_length)
        
        return N - longest_mountain

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        """
        Version 3: Patience Sorting Algorithm - The Optimized Solution
        
        Approach: Use binary search with "patience sorting" to find LIS/LDS
        efficiently. Maintains array of smallest tail elements for each length.
        
        Time Complexity: O(N log N) - Binary search for each element
        Space Complexity: O(N) - Tails array + length arrays
        
        Key insight: We don't need the actual subsequence, just its length.
        The 'tails' array maintains: tails[i] = smallest ending value of all
        increasing subsequences of length i+1.
        
        This is the production-ready solution - fast and memory efficient.
        """
        N = len(nums)
        
        def bisect_left(arr, x):
            """Binary search to find insertion position"""
            l, r = 0, len(arr)
            while l < r:
                mid = (l + r) // 2
                if arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        # Phase 1: Calculate LIS ending at each position
        lis_ending = [0] * N
        tails = []  # tails[i] = smallest tail of LIS with length i+1
        
        for i in range(N):
            # Find where nums[i] would be inserted to maintain sorted order
            pos = bisect_left(tails, nums[i])

            # Length of LIS ending at i is pos + 1
            lis_ending[i] = pos + 1

            # Update tails array
            if pos == len(tails):
                # nums[i] is larger than all tails, extend the array
                tails.append(nums[i])
            else:
                # Replace tails[pos] with smaller value to allow longer sequences
                tails[pos] = nums[i]

        # Phase 2: Calculate LDS starting at each position
        # (Same as LIS but traversing from right to left)
        lds_starting = [0] * N
        tails = []  # Reset for second pass

        for i in range(N-1, -1, -1):
            pos = bisect_left(tails, nums[i])
            lds_starting[i] = pos + 1

            if pos == len(tails):
                tails.append(nums[i])
            else:
                tails[pos] = nums[i]

        # Phase 3: Find the longest valid mountain
        longest_mountain = 0
        for i in range(1, N-1):  # Peak cannot be at endpoints
            # Mountain validity check: must have increasing and decreasing parts
            if lis_ending[i] > 1 and lds_starting[i] > 1:
                # -1 because peak is counted in both sequences
                mountain_length = lis_ending[i] + lds_starting[i] - 1
                longest_mountain = max(longest_mountain, mountain_length)

        # Minimum removals = total elements - longest mountain subsequence
        return N - longest_mountain
