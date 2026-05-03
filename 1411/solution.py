class Solution:
    def numOfWays_rmd(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Generate all 12 valid row patterns (no adjacent cells same color)
        def generate_valid_rows():
            rows = []
            for c1 in range(3):
                for c2 in range(3):
                    for c3 in range(3):
                        if c1 != c2 and c2 != c3:
                            rows.append((c1, c2, c3))
            return rows
        
        valid_rows = generate_valid_rows()
        
        # Check if two rows can be adjacent (no vertical conflicts)
        @cache
        def can_follow(prev_row, curr_row):
            return all(prev_row[i] != curr_row[i] for i in range(3))
        
        @cache
        def dp(row_idx, prev_row):
            if row_idx == n:
                return 1
            
            total = 0
            for next_row in valid_rows:
                if can_follow(prev_row, next_row):
                    total = (total + dp(row_idx + 1, next_row)) % MOD
            
            return total
        
        # Start with a dummy row that conflicts with nothing
        return dp(0, (-1, -1, -1))
