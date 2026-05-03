class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] = number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        
        # Base cases - pay attention here
        dp[0] = 1  # Empty tree - ONE way to arrange nothing
        dp[1] = 1  # One node - obviously ONE tree
        
        # Build up from smaller subproblems
        for nodes in range(2, n + 1):
            # Try each value as root
            for root in range(1, nodes + 1):
                left_nodes = root - 1      # Nodes smaller than root
                right_nodes = nodes - root  # Nodes larger than root
                
                # Multiply possibilities and add to total
                dp[nodes] += dp[left_nodes] * dp[right_nodes]
        
        return dp[n]
