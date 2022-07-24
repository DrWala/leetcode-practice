import enum
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dup_set = set()
        # for i in nums:
        #     if i in dup_set:
        #         return True
        #     dup_set.add(i)
        # return False

        # This is faster, idk why
        return len(set(nums)) != len(nums)
