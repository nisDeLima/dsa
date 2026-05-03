class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def validate():
            # Check rows
            row_patterns = {}
            for row in board:
                pattern = tuple(row)
                row_patterns[pattern] = row_patterns.get(pattern, 0) + 1
            
            if len(row_patterns) != 2:
                return False
            
            patterns = list(row_patterns.keys())
            pattern1, pattern2 = patterns[0], patterns[1]
            counts = list(row_patterns.values())
            
            # Patterns must be complements
            for i in range(n):
                if pattern1[i] == pattern2[i]:
                    return False
            
            if abs(counts[0] - counts[1]) > 1:
                return False
            
            # Check columns
            col_patterns = {}
            for col in range(n):
                pattern = tuple(board[row][col] for row in range(n))
                col_patterns[pattern] = col_patterns.get(pattern, 0) + 1
            
            if len(col_patterns) != 2:
                return False
            
            patterns = list(col_patterns.keys())
            pattern1, pattern2 = patterns[0], patterns[1]
            counts = list(col_patterns.values())
            
            for i in range(n):
                if pattern1[i] == pattern2[i]:
                    return False
            
            if abs(counts[0] - counts[1]) > 1:
                return False
            
            return True
        
        if not validate():
            return -1
        
        def min_swaps(line):
            # There are two possible target patterns:
            # Pattern A: starts with 0 -> [0, 1, 0, 1, 0, 1, ...]
            # Pattern B: starts with 1 -> [1, 0, 1, 0, 1, 0, ...]
            
            # Build Pattern A: alternating starting with 0
            pattern_start_with_0 = []
            for i in range(n):
                if i % 2 == 0:
                    pattern_start_with_0.append(0)
                else:
                    pattern_start_with_0.append(1)
            
            # Build Pattern B: alternating starting with 1
            pattern_start_with_1 = []
            for i in range(n):
                if i % 2 == 0:
                    pattern_start_with_1.append(1)
                else:
                    pattern_start_with_1.append(0)
            
            # Count how many positions don't match Pattern A
            mismatches_pattern_a = 0
            for i in range(n):
                if line[i] != pattern_start_with_0[i]:
                    mismatches_pattern_a += 1
            
            # Count how many positions don't match Pattern B
            mismatches_pattern_b = 0
            for i in range(n):
                if line[i] != pattern_start_with_1[i]:
                    mismatches_pattern_b += 1
            
            # Key insight: Each swap fixes 2 wrong positions
            # So we need (mismatches / 2) swaps
            swaps_for_pattern_a = mismatches_pattern_a // 2
            swaps_for_pattern_b = mismatches_pattern_b // 2
            
            # For odd-length boards, only ONE pattern is valid
            if n % 2 == 1:
                # Count 0s and 1s in the current line
                count_zeros = sum(1 for x in line if x == 0)
                count_ones = sum(1 for x in line if x == 1)
                
                # For odd n, one number appears (n+1)/2 times, other appears n/2 times
                # If more 0s, we MUST use pattern starting with 0
                if count_zeros > count_ones:
                    return swaps_for_pattern_a
                else:  # More 1s, we MUST use pattern starting with 1
                    return swaps_for_pattern_b
            else:
                # For even-length boards, both patterns are valid
                # Pick whichever needs fewer swaps
                return min(swaps_for_pattern_a, swaps_for_pattern_b)
        
        # Calculate swaps needed for the first row
        row_swaps = min_swaps(board[0])
        
        # Calculate swaps needed for the first column
        first_column = [board[i][0] for i in range(n)]
        col_swaps = min_swaps(first_column)
        
        return row_swaps + col_swaps
