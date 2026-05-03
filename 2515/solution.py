class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        L = len(words)
        dist_right = 0
        found = False

        for i in range(startIndex, startIndex + L):
            curr = words[i % L]
            if curr == target:
                found = True
                break
            dist_right += 1

        dist_left = 0 
        for i in range(startIndex, -(L - startIndex) - 1, -1):
            curr = words[i % L]
            if curr == target:
                found = True
                break
            dist_left += 1
        
        return min(dist_left, dist_right) if found else -1



