class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = set([1])

        while heap:
            curr = heapq.heappop(heap)
            n -= 1
            if n == 0:
                return curr

            for num in (curr * 2, curr * 3, curr * 5):
                if num not in visited:
                    visited.add(num)
                    heapq.heappush(heap, num)

