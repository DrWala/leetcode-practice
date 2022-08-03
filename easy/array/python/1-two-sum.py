import enum
from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = defaultdict(list)
        # for idx, n in enumerate(nums):
        #     nums_dict[n].append(idx)

        # for idx, n in enumerate(nums):
        #     if target - n in nums_dict:
        #         if target - n == n:
        #             if len(nums_dict[target - n]) == 1:
        #                 continue
        #             else:
        #                 return (idx, nums_dict[target - n][1])

        #         return (idx, nums_dict[target - n][0])
        ##
        for idx, n in enumerate(nums):
            if target - n in nums_dict:
                return (idx, nums_dict[target - n][0])
            else:
                nums_dict[n].append(idx)
