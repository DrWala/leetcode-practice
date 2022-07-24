from collections import Counter
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ctr = Counter(nums)

        i = 0
        if 0 in ctr:
            count = ctr[0]
            lim = count + i
            while i < lim:
                nums[i] = 0
                i += 1

        if 1 in ctr:
            count = ctr[1]
            lim = count + i
            while i < lim:
                nums[i] = 1
                i += 1

        if 2 in ctr:
            count = ctr[2]
            lim = count + i
            while i < lim:
                nums[i] = 2
                i += 1


nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums)
print(nums)
nums = [2, 0, 1]
Solution().sortColors(nums)
print(nums)
nums = [0]
Solution().sortColors(nums)
print(nums)
nums = [1]
Solution().sortColors(nums)
print(nums)
