class Solution_rmvd:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        score = []
        m = arr[(len(arr) - 1) // 2]

        for i in range(len(arr)):
            score.append((abs(arr[i] - m), arr[i]))
        
        score.sort(reverse=True)

        return [num for score, num in score[:k]]
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        score = []
        m = arr[(len(arr) - 1) // 2]
        heap = []
        for i in range(len(arr)):
            heapq.heappush(heap, (abs(arr[i] - m), arr[i]))
            if len(heap) > k:
                heapq.heappop(heap)
        

        return [num for score, num in heap]
