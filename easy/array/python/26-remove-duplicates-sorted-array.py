from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_idx = 0
        next_idx = 1
        while next_idx < len(nums):
            if nums[curr_idx] != nums[next_idx]:
                nums[curr_idx + 1] = nums[next_idx]
                curr_idx += 1
            next_idx += 1
        return curr_idx


nums = [1, 1, 2]
Solution().removeDuplicates(nums)
print(nums)

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Solution().removeDuplicates(nums)
print(nums)

nums = [1, 1]
Solution().removeDuplicates(nums)
print(nums)
