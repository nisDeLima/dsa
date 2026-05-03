class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        merge_queue = deque([])
        res = []

        for char in s:
            if len(merge_queue) > k:
                merge_queue.popleft()
            if char not in merge_queue:
                res.append(char)
                merge_queue.append(char)
            else:
                continue

        return "".join(res)
