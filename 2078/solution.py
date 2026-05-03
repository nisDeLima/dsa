class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        from_left = 0
        from_right = 0

        for i in range(1, len(colors)):
            if colors[i] != colors[0]:
                from_left = i

        for j in range(len(colors) - 2, -1, -1):
            if colors[j] != colors[len(colors) - 1]:
                from_right = len(colors) - j - 1
        
        return max(from_left, from_right)
