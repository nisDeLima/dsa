class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        i = 0  # passenger index
        filled = 0  # seats filled in last bus

        # simulate boarding
        for bus in buses:
            filled = 0
            while i < len(passengers) and passengers[i] <= bus and filled < capacity:
                i += 1
                filled += 1

        # Case 1: last bus has free seats
        if filled < capacity:
            ans = buses[-1]
        else:
            # last boarded passenger index = i - 1
            cand = i - 1
            ans = passengers[cand] - 1

        # ensure ans not equal to a passenger arrival
        passenger_set = set(passengers)
        while ans in passenger_set:
            ans -= 1

        return ans

