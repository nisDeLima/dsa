class Solution:
    def numSteps_rmvd(self, s: str) -> int:
        count = 0
        curr = int(s, 2)
        while curr != 1:
            if curr % 2 == 0:
                curr //= 2
            else:
                curr += 1
            count += 1
        return count
    def numSteps(self, s: str) -> int:
        s = list(s)
        steps = 0
        while len(s) > 1:
            if s[-1] == '0':
                s.pop()
            else:
                # add 1: propagate carry
                i = len(s) - 1
                while i >= 0 and s[i] == '1':
                    s[i] = '0'
                    i -= 1
                if i < 0:
                    s.insert(0, '1')
                else:
                    s[i] = '1'
            steps += 1
        return steps
