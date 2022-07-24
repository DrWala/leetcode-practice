from typing import List
import math


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs_len = len(cost)

        def mincost(i):
            if i >= costs_len:
                return 0
            else:
                return cost[i] + min(mincost(i + 1), mincost(i + 2))

        return min(mincost(0), mincost(1))


print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
