class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        # Rule 1: The non-X characters must be in the same order
        # Can't create or destroy R's and L's, just move them
        if start.replace('X', '') != result.replace('X', ''):
            return False
        
        # Rule 2: R can only move right (never pass another R or L)
        # L can only move left (never pass another L or R)
        i = j = 0
        n = len(start)
        
        while i < n and j < n:
            # Skip X's in start
            while i < n and start[i] == 'X':
                i += 1
            # Skip X's in result
            while j < n and result[j] == 'X':
                j += 1
            
            # Both exhausted = valid
            if i == n and j == n:
                return True
            # One exhausted but not the other = invalid
            if i == n or j == n:
                return False
            
            # Characters must match
            if start[i] != result[j]:
                return False
            
            # R can only move right: position in result >= position in start
            if start[i] == 'R' and j < i:
                return False
            # L can only move left: position in result <= position in start  
            if start[i] == 'L' and j > i:
                return False
            
            i += 1
            j += 1
        
        return True
