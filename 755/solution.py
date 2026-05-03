class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        for _ in range(volume):
            # Try flowing left first
            best = k
            
            # Scan left from k-1 to 0
            for i in range(k - 1, -1, -1):
                if heights[i] > heights[best]:
                    break  # Hit a wall going up, stop
                if heights[i] < heights[best]:
                    best = i  # Found lower ground, update best
                # If equal, keep going but remember this position
            
            # If we stayed at k (couldn't go left), try right
            if best == k:
                for i in range(k + 1, len(heights)):
                    if heights[i] > heights[best]:
                        break  # Hit a wall going up, stop
                    if heights[i] < heights[best]:
                        best = i  # Found lower ground, update best
            
            # Drop the water at the best position
            heights[best] += 1
        
        return heights
