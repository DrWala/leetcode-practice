from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        best_profit = 0
        while sell < len(prices):
            curr_profit = prices[sell] - prices[buy]
            if curr_profit <= 0:
                buy = sell
                sell = sell + 1
            else:  # We can make a profit, lets make moneu
                best_profit += curr_profit
                buy = sell
                sell = sell + 1
        return best_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
