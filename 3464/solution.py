class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:

        def to_perimeter(x: int, y: int) -> int:
            if y == 0:
                return x
            if x == side:
                return side + y
            if y == side:
                return 2 * side + (side - x)
            return 3 * side + (side - y)

        perimeter_points = sorted(to_perimeter(x, y) for x, y in points)
        perimeter_length = 4 * side
        n = len(perimeter_points)

        def can_place(min_dist: int) -> bool:
            for start in range(n):

                if perimeter_points[start] > perimeter_points[0] + min_dist:
                    break

                first = perimeter_points[start]
                current = first
                chosen = 1

                while chosen < k:
                    next_index = bisect_left(perimeter_points, current + min_dist)

                    if next_index == n:
                        break

                    current = perimeter_points[next_index]
                    chosen += 1

                if chosen < k:
                    continue

                circular_gap = perimeter_length - (current - first)

                if circular_gap >= min_dist:
                    return True

            return False

        low = 0
        high = perimeter_length // k

        while low <= high:
            mid = (low + high) // 2

            if can_place(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high
