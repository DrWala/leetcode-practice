from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # store last k somewhere
        temp = [0] * n
        # move n-k elems to the right
        for i in range(0, n-k):
            temp[i+k] = nums[i]
        # move temp back
        for i in range(0, k):
            temp[i] = nums[i-k]

        # Copy back to nums
        for i in range(len(temp)):
            nums[i] = temp[i]


print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 1))
print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 2))
print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))
