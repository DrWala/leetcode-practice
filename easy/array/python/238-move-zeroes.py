import enum
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            curr = nums[fast]
            prev = nums[slow]

            if prev != 0:
                slow += 1

            if curr != 0 and prev == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1


nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)
nums = [1, 2, 3, 4]
Solution().moveZeroes(nums)
print(nums)
nums = [1]
Solution().moveZeroes(nums)
print(nums)
nums = [0, 0, 0]
Solution().moveZeroes(nums)
print(nums)
nums = [0, 1, 0]
Solution().moveZeroes(nums)
print(nums)
nums = [0, 1, 2]
Solution().moveZeroes(nums)
print(nums)
nums = [1, 0, 1]
Solution().moveZeroes(nums)
print(nums)
