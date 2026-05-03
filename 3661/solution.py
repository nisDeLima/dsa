#       Input: robots = [4], distance = [3], walls = [1,10]
#
#
#       0 1 2 3 4 5 6 7 8 9 10                       (furthest_wall)
#         |     r            |
#
#        1 1 -1 -1 10 10 10 10 10 10 
#      -1  1 1  1 -1  -1 -1 -1 -1 10
#
#robots = [10,2], distance = [5,1], walls = [5,2,7]
#
#    0  1  2  3  4  5  6  7  8  9  10
#    --------------------------------->
#r         1                        0
#w         w        w     w

#class Solution:
#    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
#        # Setup data
#        robots_info = list(zip(robots, distance))
#        robots_info.sort()
#
#        walls_info = [(position, idx) for idx, position in enumerate(walls)]
#        walls_info.sort()
#        #################
#
#        walls_to_right = []
#        walls_to_left = []
#
#        walls_idx = 0
#        for robot_pos, rang in robots_info:
#            left_walls = []
#            while walls_idx < len(walls_info) and robot_pos >= walls_info[walls_idx][0]:
#                w_pos, w_idx = walls_info[walls_idx]
#                if robot_pos - w_pos <= rang:
#                    left_walls.append(w_idx)
#                walls_idx += 1
#            walls_to_left.append(left_walls)
#
#        walls_idx = len(walls_info) - 1
#        for robot_pos, rang in reversed(robots_info):
#            right_walls = []
#            while walls_idx >= 0 and robot_pos <= walls_info[walls_idx][0]:
#                w_pos, w_idx = walls_info[walls_idx]
#                if w_pos - robot_pos <= rang:
#                    right_walls.append(w_idx)
#                walls_idx -= 1
#            walls_to_right.append(right_walls)
#
#        walls_to_right.reverse()
#
#        n = len(robots_info)
#
#        @cache
#        def dp(i, destroyed):
#            if i == n:
#                return 0
#
#            # Option 1: don't shoot
#            best = dp(i + 1, destroyed)
#
#            # Option 2: shoot left
#            new_left = frozenset(w for w in walls_to_left[i] if w not in destroyed)
#            best = max(best, len(new_left) + dp(i + 1, destroyed | new_left))
#
#            # Option 3: shoot right
#            new_right = frozenset(w for w in walls_to_right[i] if w not in destroyed)
#            best = max(best, len(new_right) + dp(i + 1, destroyed | new_right))
#
#            return best
#
#        return dp(0, frozenset())
class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # Setup data
        robots_info = list(zip(robots, distance))
        robots_info.sort()

        walls_info = [(position, idx) for idx, position in enumerate(walls)]
        walls_info.sort()
        #################

        walls_to_right = []
        walls_to_left = []

        walls_idx = 0
        for robot_pos, rang in robots_info:
            left_walls = []
            while walls_idx < len(walls_info) and robot_pos >= walls_info[walls_idx][0]:
                w_pos, w_idx = walls_info[walls_idx]
                if robot_pos - w_pos <= rang:
                    left_walls.append(w_idx)
                walls_idx += 1
            walls_to_left.append(left_walls)

        walls_idx = len(walls_info) - 1
        for robot_pos, rang in reversed(robots_info):
            right_walls = []
            while walls_idx >= 0 and robot_pos <= walls_info[walls_idx][0]:
                w_pos, w_idx = walls_info[walls_idx]
                if w_pos - robot_pos <= rang:
                    right_walls.append(w_idx)
                walls_idx -= 1
            walls_to_right.append(right_walls)

        walls_to_right.reverse()

        n = len(robots_info)

        @cache
        def dp(i, prev_shot_right):
            if i == n:
                return 0

            left_set = set(walls_to_left[i])
            right_set = set(walls_to_right[i])

            # If previous robot shot right, remove overlapping walls from my left
            if prev_shot_right:
                left_set -= set(walls_to_right[i - 1])

            left_count = len(left_set)
            right_count = len(right_set)

            # Option 1: don't shoot
            best = dp(i + 1, False)

            # Option 2: shoot left
            best = max(best, left_count + dp(i + 1, False))

            # Option 3: shoot right
            best = max(best, right_count + dp(i + 1, True))

            return best

        return dp(0, False)
