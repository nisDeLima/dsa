class NumberContainers:

    def __init__(self):
        self.num_to_idx = defaultdict(list)
        self.idx_to_num = {}


    def change(self, index: int, number: int) -> None:
        self.idx_to_num[index] = number
        heapq.heappush(self.num_to_idx[number], index)

    def find(self, number: int) -> int:
        res = -1
        while self.num_to_idx[number]:
            if self.idx_to_num[self.num_to_idx[number][0]] != number:
                heapq.heappop(self.num_to_idx[number])
                continue 
            else:
                res = self.num_to_idx[number][0]
                break 
        return res
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
