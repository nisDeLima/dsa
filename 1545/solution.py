class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            inverted = []
            for c in s:
                if c == "0":
                    inverted.append("1")
                else:
                    inverted.append("0")
            return "".join(inverted)

        s = "0"
        for i in range(2, n + 1): 
            si = s + "1" + "".join(reversed(invert(s)))
            s = si

        return s[k - 1]
