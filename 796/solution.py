class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        N = len(s)
        if N != len(goal):
            return False
        start_letter = goal[0]

        candidates_idx = []

        def check(cand):
            g_idx = 0
            s_idx = cand
            for i in range(N):
                if goal[g_idx] != s[s_idx % N]:
                    return False
                g_idx += 1
                s_idx += 1

            return True

        for idx, ltr in enumerate(s):
            if ltr == start_letter:
                candidates_idx.append(idx)
        
        for cand in candidates_idx:
            if check(cand):
                return True

        return False
