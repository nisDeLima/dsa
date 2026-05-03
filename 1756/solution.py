from sortedcontainers import SortedList
class MRUQueue:
    def __init__(self, n: int):
        self.sl = SortedList()
        for i in range(n):
            self.sl.add((i, i + 1))
        self.inc = n

    def fetch(self, k: int) -> int:
        elm = self.sl[k - 1]
        self.sl.remove(elm)
        self.sl.add((self.inc, elm[1]))
        self.inc += 1
        return elm[1]

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
