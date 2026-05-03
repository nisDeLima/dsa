class Solution:
    def averageWaitingTime_rmd(self, customers: List[List[int]]) -> float:
        queue = deque(customers)

        wait_times = []
        curr_time = 1

        while queue:
            arrival, time = queue.popleft()
            curr_time = max(curr_time, arrival)
            # add prep time
            curr_time += time
            # add total wait time
            wait_times.append(curr_time - arrival)
        
        L = len(wait_times)
        return sum(wait_times) / L
    def averageWaitingTime_rmvd2(self, customers: List[List[int]]) -> float:
        wait_times = []
        curr_time = 1

        for arrival, time in customers:
            curr_time = max(curr_time, arrival)
            # add prep time
            curr_time += time
            # add total wait time
            wait_times.append(curr_time - arrival)
        
        L = len(wait_times)
        return sum(wait_times) / L
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_time = 0
        total_wait = 0
        
        for arrival, prep in customers:
            curr_time = max(curr_time, arrival) + prep
            total_wait += curr_time - arrival
        
        return total_wait / len(customers)
