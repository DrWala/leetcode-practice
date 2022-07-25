from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        first = nums[0]
        for i in range(1, len(nums)):
            first ^= nums[i]
        return first
