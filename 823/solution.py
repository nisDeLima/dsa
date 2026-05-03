class Solution:
    def numFactoredBinaryTrees_rmvd(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        # Precompute possible children
        possible_pairs = {}
        for num in arr:
            possible_pairs[num] = set()

        for num in arr:
            for num2 in arr:
                if (num * num2) in possible_pairs:
                    possible_pairs[num * num2].add((num, num2))
                    possible_pairs[num * num2].add((num2, num))
        @cache
        def combine_children(num):
            res = 1

            for pair in possible_pairs[num]:
                x, y = pair
                res = (res + combine_children(x) * combine_children(y)) % MOD

            return res

        res = 0
        for num in arr:
            res = (res + combine_children(num)) % MOD

        return res
        
    def numFactoredBinaryTrees_rmvd2(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        
        num_set = set(arr)  # O(1) lookup
        dp = {}  # Store results as we go
        
        for num in arr:
            dp[num] = 1  # Each number is a tree by itself
            
            for left in arr:
                if left >= num:  # No point checking bigger numbers
                    break
                    
                if num % left == 0:  # Check if left divides num
                    right = num // left
                    if right in num_set:
                        dp[num] = (dp[num] + dp[left] * dp[right]) % MOD
        
        return sum(dp.values()) % MOD
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        
        num_to_idx = {num: i for i, num in enumerate(arr)}
        dp = [1] * len(arr)  # Each number is a tree by itself
        
        for i, num in enumerate(arr):
            # Binary search boundary: only check left values smaller than sqrt(num)
            for j in range(i):  # j < i means arr[j] < num (sorted!)
                left = arr[j]
                
                if left * left > num:  # Optimization: stop when left > sqrt(num)
                    break
                    
                if num % left == 0:
                    right = num // left
                    if right in num_to_idx:
                        right_idx = num_to_idx[right]
                        if left == right:
                            dp[i] = (dp[i] + dp[j] * dp[j]) % MOD
                        else:
                            # Count both (left, right) and (right, left)
                            dp[i] = (dp[i] + 2 * dp[j] * dp[right_idx]) % MOD
        
        return sum(dp) % MOD 
