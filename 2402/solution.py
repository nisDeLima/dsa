class Solution:
    def mostBooked(self, n, meetings):
        available = list(range(n))
        heapq.heapify(available)
        occupied = []  # (release_time, room_id)
        rooms_count = [0] * n
    
        meetings.sort()
    
        for start, end in meetings:
            while occupied and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(available, room)
    
            if available:
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))
            else:
                release, room = heapq.heappop(occupied)
                heapq.heappush(occupied, (end + release - start, room))
    
            rooms_count[room] += 1
    
        return rooms_count.index(max(rooms_count))
