from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Naive
        # nums = sorted(nums, reverse=True)
        # return nums[k - 1]
        # Smart
        return heapq.nlargest(n=k, iterable=nums)[-1]
