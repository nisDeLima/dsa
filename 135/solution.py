class Solution:
    def candy(self, ratings: List[int]) -> int:
        lower_ahead = [0] * len(ratings)
        for i in range(len(ratings) - 2, -1, -1):
            curr = 0
            if ratings[i] > ratings[i + 1]:
                curr += 1 + lower_ahead[i + 1]
            lower_ahead[i] = curr
        
        candies = []
        prev = float("inf")
        
        for idx, next_l in enumerate(lower_ahead):
            if ratings[idx] > prev:
                value = max(candies[-1] + 1, lower_ahead[idx] + 1)
            else:
                value = max(1, lower_ahead[idx] + 1)
            
            candies.append(value)
            prev = ratings[idx]
        
        return sum(candies)
