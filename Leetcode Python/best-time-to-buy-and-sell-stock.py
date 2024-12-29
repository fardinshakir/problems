# Need to solve
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        O(N^2)
        best = 0
        for i, start_day in enumerate(prices):
            for others in range(i+1, len(prices)):
                current_value = -(start_day - prices[others])
                if current_value > best:

                    best = current_value
        return best
        """
        """
        O(N) slow
        min_price = float('inf')
        max_price = 0
        for current in prices:
            min_price = min(min_price, current)
            profit = current - min_price
            max_price = max(max_price, profit)
        return max_price
        """
        """
        O(N) faster
        """
        min_price = prices[0]
        max_profit = 0
        for current in prices:
            if current < min_price:
                min_price = current
            profit = current - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit
if __name__ == "__main__":
    solution = Solution()
    prices = [7,1,5,3,6,4]
    result = solution.maxProfit(prices)
    print(result)
