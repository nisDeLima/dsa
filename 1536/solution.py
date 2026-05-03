class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Trailing zeroes per row
        trailing = []
        for row in grid:
            count = 0
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        moves = 0
        for i in range(n):
            required = n - 1 - i
            
            # Find the first row at or below i with enough trailing zeroes
            target = -1
            for j in range(i, n):
                if trailing[j] >= required:
                    target = j
                    break
            
            if target == -1:
                return -1  # Impossible
            
            # Bubble it up to position i
            while target > i:
                trailing[target], trailing[target - 1] = trailing[target - 1], trailing[target]
                target -= 1
                moves += 1
        
        return moves
