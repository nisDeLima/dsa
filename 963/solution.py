class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        def distance(p1, p2):
            d = (p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2
            return d

        pts = set()

        ans = sys.maxsize

        for p1 in points:
            for p2 in pts:
                if p1 == p2:
                    continue

                for p3 in pts:
                    if p3 not in [p1, p2] and distance(p1, p2) + distance(p2, p3) == distance(p1, p3):
                        x4 = p1[0] + p3[0] - p2[0]
                        y4 = p1[1] + p3[1] - p2[1]

                        if (x4, y4) in pts:
                            area = sqrt(distance(p1,p2)) * sqrt(distance(p2,p3))
                            ans = min(ans, area)
            pts.add((p1[0], p1[1]))

        return ans if ans < sys.maxsize else 0
