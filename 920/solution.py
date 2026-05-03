class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @cache
        def helper(curr_goal, unique_songs):
            if curr_goal == 0 and unique_songs == n:
                return 1
            if curr_goal == 0 or unique_songs > n:
                return 0

            take = (n - unique_songs) * helper(curr_goal - 1, unique_songs + 1)

            if unique_songs > k:
                take += (unique_songs - k) * helper(curr_goal - 1, unique_songs)

            return take

        return helper(goal, 0) % (10**9 + 7)
