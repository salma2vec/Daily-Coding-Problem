class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        min_price = prices[0]  # Initialize the minimum price to the first day's price
        max_profit = 0  # Initialize the maximum profit to 0
        
        for price in prices:
            min_price = min(min_price, price)  # Update the minimum price if a smaller price is found
            max_profit = max(max_profit, price - min_price)  # Calculate and update the maximum profit
        return max_profit        