class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        # Base case - can't screw up a single element
        if n == 1:
            return [1]
        
        # Recursively build a beautiful array for roughly half the size
        smaller = self.beautifulArray((n + 1) // 2)
        
        # Transform into odds: 2*x - 1
        # This maps [1,2,3...] into [1,3,5...]
        odds = [2 * x - 1 for x in smaller]
        
        # Transform into evens: 2*x
        # This maps [1,2,3...] into [2,4,6...]
        evens = [2 * x for x in smaller if 2 * x <= n]
        
        # Odds first, then evens - the sacred separation
        return odds + evens
