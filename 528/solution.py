class Solution:
    def __init__(self, w: List[int]):
        self.pool = []
        self.total = sum(w)
        prev = 0
        for elm in w:
            self.pool.append(elm + prev)
            prev = elm + prev
    def pickIndex(self) -> int:
        get = random.randint(1, self.total)

        for idx, num in enumerate(self.pool):
            if get <= num:
                return idx
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
