from functools import cache

class Solution:
    def maxA(self, n: int) -> int:
        @cache
        def dfs(keystrokes_left):
            if keystrokes_left <= 0:
                return 0

            # Option 1: press A
            best = dfs(keystrokes_left - 1) + 1

            # Option 2: at some earlier keystroke, freeze the screen,
            # ctrl+a, ctrl+c, then spam ctrl+v with the rest
            for freeze_at in range(1, keystrokes_left - 1):
                pastes = keystrokes_left - freeze_at - 2  # minus 2 for ctrl+a, ctrl+c
                as_on_screen = dfs(freeze_at)
                best = max(best, as_on_screen * (pastes + 1))

            return best

        return dfs(n)
