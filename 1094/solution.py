class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips_m = [] # start, to, num_passengers

        for num, start, to in trips:
            trips_m.append((start, to, num))
        
        trips_m.sort(reverse=True)

        pq = [] # free_point, num_pass
        while trips_m:
            start, to, num_pass = trips_m.pop()

            while pq and pq[0][0] <= start:
                _, free_spots = heapq.heappop(pq)
                capacity += free_spots

            capacity -= num_pass
            if capacity < 0:
                return False
            heapq.heappush(pq, (to, num_pass))

        return True
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for num, start, end in trips:
            events.append((start, num))    # people get in
            events.append((end, -num))     # people get out

        events.sort()

        current = 0
        for _, change in events:
            current += change
            if current > capacity:
                return False

        return True

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = {}
        max_km = 0

        for num, start, end in trips:
            timeline[start] = timeline.get(start, 0) + num
            timeline[end] = timeline.get(end, 0) - num
            if end > max_km:
                max_km = end

        current = 0
        for km in range(0, max_km + 1):
            if km in timeline:
                current += timeline[km]
            if current > capacity:
                return False

        return True
