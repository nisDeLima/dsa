class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []

        def backtrack(i, curr):
            if i >= len(word):
                res.append("".join(curr))
                return
            curr.append(word[i])
            backtrack(i + 1, curr)
            curr.pop()
            curr_num = 0
            for j in range(i, len(word)):
                curr_num += 1
                if j < len(word) - 1:
                    curr.append(str(curr_num))
                    curr.append(word[j + 1])
                    backtrack(j + 2, curr)
                    curr.pop()
                    curr.pop()
                else:
                    curr.append(str(curr_num))
                    backtrack(j + 1, curr)
                    curr.pop()

        backtrack(0, [])

        return res
        
