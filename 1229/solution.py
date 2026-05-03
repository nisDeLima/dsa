class Solution:
    def minAvailableDuration_rmd(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # time, event_type, person_id
        events = []

        for s, e in slots1:
            events.append((s, "start", 1))
            events.append((e, "end", 1))
        for s, e in slots2:
            events.append((s, "start", 2))
            events.append((e, "end", 2))
        
        events.sort()
        intersection_time = 0
        people_avail = [False, False]
        last_avail_time = float("-inf")
        for time, event_type, person_id in events:
            if all(people_avail) and time - last_avail_time >= duration:
                return [last_avail_time, last_avail_time + duration]
            if event_type == "start":
                people_avail[person_id - 1] = True
                last_avail_time = time
            if event_type == "end":
                people_avail[person_id - 1] = False
        
        return []



    def minAvailableDuration(self, slots1, slots2, duration):
        slots1.sort()
        slots2.sort()
        i = j = 0
        while i < len(slots1) and j < len(slots2):
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if end - start >= duration:
                return [start, start + duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []
