class ExamRoom_TLE:
    def __init__(self, n: int):
        self.seats = [0] * n
    
    def seat(self) -> int:
        # If room is empty, sit at position 0
        if sum(self.seats) == 0:
            self.seats[0] = 1
            return 0
        
        max_dist = 0
        best_seat = 0
        
        def distance_to_nearest(i):
            # Find closest occupied seat to the left
            left_dist = float('inf')
            for j in range(i - 1, -1, -1):
                if self.seats[j] == 1:
                    left_dist = i - j
                    break
            
            # Find closest occupied seat to the right
            right_dist = float('inf')
            for j in range(i + 1, len(self.seats)):
                if self.seats[j] == 1:
                    right_dist = j - i
                    break
            
            # Return the minimum distance to ANY occupied seat
            return min(left_dist, right_dist)
        
        # Check every empty seat
        for i in range(len(self.seats)):
            if self.seats[i] == 0:
                dist = distance_to_nearest(i)
                if dist > max_dist:
                    max_dist = dist
                    best_seat = i
        
        self.seats[best_seat] = 1
        return best_seat
    
    def leave(self, p: int) -> None:
        self.seats[p] = 0
class ExamRoom_AlsoTLE:
    def __init__(self, n: int):
        self.seats = [0] * n
    
    def seat(self) -> int:
        # If room is empty, sit at position 0
        if sum(self.seats) == 0:
            self.seats[0] = 1
            return 0
        
        max_dist = 0
        best_seat = 0
        
        def distance_to_nearest():
            dist_left = [float("inf")] * len(self.seats)
            dist_right = [float("inf")] * len(self.seats)
            
            curr = float("inf")
            for i in range(len(self.seats)):
                if self.seats[i] == 1:
                    curr = 0
                else:
                    curr += 1
                dist_left[i] = curr

            curr = float("inf")
            for i in range(len(self.seats) - 1, -1, -1):
                if self.seats[i] == 1:
                    curr = 0
                else:
                    curr += 1
                dist_right[i] = min(curr, dist_left[i])

            best_dist = 0
            best_seat = 0

            for i in range(len(self.seats)):
                if min(dist_left[i], dist_right[i]) > best_dist:
                    best_dist = min(dist_left[i], dist_right[i])
                    best_seat = i
            
            return best_seat

        best_seat = distance_to_nearest()
        self.seats[best_seat] = 1
        return best_seat
    
    def leave(self, p: int) -> None:
        self.seats[p] = 0


class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class SortedSet:
    def __init__(self):
        self.start = Node(None)
    
    def add(self, val):
        prev, curr = self.start, self.start.next
        
        while curr and curr.val < val:
            prev = curr
            curr = curr.next
        
        # Insert between prev and curr
        new_node = Node(val, prev, curr)
        prev.next = new_node
        if curr:
            curr.prev = new_node
    
    def remove(self, val):
        curr = self.start.next
        
        while curr and curr.val != val:
            curr = curr.next
        
        if curr:  # Found it
            curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
    
    def __iter__(self):
        curr = self.start.next
        while curr:
            yield curr.val
            curr = curr.next

class ExamRoom_rmvd:
    def __init__(self, n: int):
        self.sorted_set = SortedSet()
        self.size = n
    
    def seat(self) -> int:
        positions = list(self.sorted_set)
        
        if not positions:
            self.sorted_set.add(0)
            return 0
        
        # Check seat 0
        best_dist = positions[0]
        best_seat = 0
        
        # Check intervals between consecutive occupied seats
        for i in range(len(positions) - 1):
            left, right = positions[i], positions[i + 1]
            mid = left + (right - left) // 2
            dist = mid - left  # Distance to nearest occupied
            
            if dist > best_dist:
                best_dist = dist
                best_seat = mid
        
        # Check seat n-1
        if self.size - 1 - positions[-1] > best_dist:
            best_seat = self.size - 1
        
        self.sorted_set.add(best_seat)
        return best_seat
    
    def leave(self, p: int) -> None:
        self.sorted_set.remove(p)

import heapq

class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.heap = []
        # Start with one interval covering the entire room
        # Negative distance for max-heap behavior
        heapq.heappush(self.heap, (-self._distance(0, n - 1), 0, n - 1))
    
    def seat(self) -> int:
        # Pop interval with maximum distance
        neg_dist, left, right = heapq.heappop(self.heap)
        
        # Determine optimal seat in this interval
        if left == 0:
            seat_pos = 0
        elif right == self.n - 1:
            seat_pos = self.n - 1
        else:
            # Sit in the middle of the interval
            seat_pos = left + (-neg_dist)
        
        # Split interval: add left portion if it exists
        if seat_pos > left:
            new_left_interval = (left, seat_pos - 1)
            heapq.heappush(self.heap, (
                -self._distance(*new_left_interval),
                *new_left_interval
            ))
        
        # Split interval: add right portion if it exists
        if seat_pos < right:
            new_right_interval = (seat_pos + 1, right)
            heapq.heappush(self.heap, (
                -self._distance(*new_right_interval),
                *new_right_interval
            ))
        
        return seat_pos
    
    def leave(self, p: int) -> None:
        # Find intervals adjacent to the leaving position
        left_interval = None   # Interval ending at p-1
        right_interval = None  # Interval starting at p+1
        
        for interval in self.heap:
            _, start, end = interval
            if end == p - 1:
                left_interval = interval
            if start == p + 1:
                right_interval = interval
        
        # Determine bounds of merged interval
        new_start = left_interval[1] if left_interval else p
        new_end = right_interval[2] if right_interval else p
        
        # Remove old intervals
        if left_interval:
            self.heap.remove(left_interval)
        if right_interval:
            self.heap.remove(right_interval)
        
        # Add merged interval
        heapq.heappush(self.heap, (
            -self._distance(new_start, new_end),
            new_start,
            new_end
        ))
        
        # Restore heap property after removals
        heapq.heapify(self.heap)
    
    def _distance(self, left: int, right: int) -> int:
        """
        Calculate the maximum distance to nearest occupied seat
        for the optimal position in interval [left, right].
        """
        # Edge intervals: can sit at the edge
        if left == 0 or right == self.n - 1:
            return right - left
        
        # Middle interval: sit at midpoint
        return (right - left) // 2
