class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = []

        for emp_id, intervals in enumerate(schedule):
            for interval in intervals:
                events.append((interval.start, 1, emp_id))  # start
                events.append((interval.end, -1, emp_id))   # end

        events.sort()

        working = 0
        prev_time = None
        res = []

        for time, delta, _ in events:
            if working == 0 and prev_time is not None and prev_time < time:
                res.append(Interval(prev_time, time))

            working += delta
            prev_time = time

        return res
