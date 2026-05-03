class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlaps(int1, int2):
            return min(int1[1], int2[1]) >= max(int1[0], int2[0])
        remove_from = float("inf") 
        for idx, (start, end) in enumerate(intervals):
            if overlaps((start, end), newInterval):
                remove_from = min(remove_from, idx)
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
            else:
                if start > newInterval[0]:
                    return intervals[:min(idx, remove_from)] + [newInterval] + intervals[idx:]

        return intervals[:min(remove_from, len(intervals))] + [newInterval]
