class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
            
        res_list = []
        ban_letters = deque()
        
        avail_letters = [(-cnt, ch) for ch, cnt in Counter(s).items()]
        heapq.heapify(avail_letters)

        while avail_letters:
            neg_cnt, ch = heapq.heappop(avail_letters)
            res_list.append(ch)
            ban_letters.append((neg_cnt + 1, ch))

            if len(ban_letters) == k:
                neg_cnt_back, ch_back = ban_letters.popleft()
                if neg_cnt_back < 0:
                    heapq.heappush(avail_letters, (neg_cnt_back, ch_back))

        return "".join(res_list) if len(res_list) == len(s) else ""
