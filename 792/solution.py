class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for word in words:
            it = iter(word)
            c = next(it, None)
            if c:
                waiting[c].append(it)
            else:
                waiting[None].append(it)

        count = 0
        for char in s:
            current_waiting = waiting[char]
            waiting[char] = []

            for word_iter in current_waiting:
                next_char = next(word_iter, None)
                if next_char is None:
                    count += 1
                else:
                    waiting[next_char].append(word_iter)

        count += len(waiting[None])
        return count
