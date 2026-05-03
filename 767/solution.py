class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_heap = [(-count, letter) for letter, count in counter.items()]
        heapq.heapify(max_heap)
        res = []

        while max_heap:
            curr_count, curr = heapq.heappop(max_heap)
            if res:
                if curr == res[-1]:
                    if not max_heap:
                        return ""
                    else:
                        second_count, second_curr = heapq.heappop(max_heap)
                        res.append(second_curr)
                        heapq.heappush(max_heap,(curr_count, curr))
                        if second_count + 1 < 0:
                            heapq.heappush(max_heap,(second_count + 1, second_curr))
                        continue
            res.append(curr)
            if curr_count + 1 < 0:
                heapq.heappush(max_heap, (curr_count + 1, curr))

        return "".join(res)
