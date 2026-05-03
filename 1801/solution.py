class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        
        # Max heap for buy orders (negate prices), min heap for sell orders
        buy_heap = []   # (-price, amount)
        sell_heap = []  # (price, amount)
        
        for price, amount, order_type in orders:
            if order_type == 0:  # Buy order
                # Match with sell orders
                while amount and sell_heap and sell_heap[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell_heap)
                    matched = min(amount, sell_amount)
                    amount -= matched
                    if sell_amount > matched:
                        heapq.heappush(sell_heap, (sell_price, sell_amount - matched))
                
                # Add remaining to backlog
                if amount:
                    heapq.heappush(buy_heap, (-price, amount))
            
            else:  # Sell order
                # Match with buy orders
                while amount and buy_heap and -buy_heap[0][0] >= price:
                    buy_price, buy_amount = heapq.heappop(buy_heap)
                    matched = min(amount, buy_amount)
                    amount -= matched
                    if buy_amount > matched:
                        heapq.heappush(buy_heap, (buy_price, buy_amount - matched))
                
                # Add remaining to backlog
                if amount:
                    heapq.heappush(sell_heap, (price, amount))
        
        # Sum up all backlog orders
        return sum(amount for _, amount in buy_heap + sell_heap) % MOD
