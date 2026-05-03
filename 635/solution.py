from typing import List

GRANULARITIES = ["Year", "Month", "Day", "Hour", "Minute", "Second"]

class LogSystem:
    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        gran_idx = GRANULARITIES.index(granularity)
        # Number of characters to compare: "2017:01:01:23:59:59"
        # Year=4, +:Month=7, +:Day=10, +:Hour=13, +:Minute=16, +:Second=19
        prefix_len = [4, 7, 10, 13, 16, 19][gran_idx]
        
        start_cmp = start[:prefix_len]
        end_cmp = end[:prefix_len]
        
        return [id for id, ts in self.logs if start_cmp <= ts[:prefix_len] <= end_cmp]
