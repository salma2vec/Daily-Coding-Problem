from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = {}

        def bs(index, holding_stock):
            if index >= len(prices):
                return 0

            if (index, holding_stock) in d:
                return d[(index, holding_stock)]

            if holding_stock:
                # If holding stock, we can either sell it today or hold
                profit = max(prices[index] + bs(index + 1, False), bs(index + 1, True))
            else:
                # If not holding stock, we can either buy it today or skip
                profit = max(-prices[index] + bs(index + 1, True), bs(index + 1, False))

            d[(index, holding_stock)] = profit
            return profit

        return bs(0, False)



        