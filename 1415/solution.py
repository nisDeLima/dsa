class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        avail = ["a", "b", "c"]
        strings = []


        def backtrack(curr):
            if len(strings) >= k:
                return
            if len(curr) == n:
                strings.append("".join(curr))
                return

            for char in avail:
                if not curr or char != curr[-1]:
                    curr.append(char)
                    backtrack(curr)
                    curr.pop()

        backtrack([])
        return strings[k - 1] if len(strings) >= k else ""
