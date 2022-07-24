from typing import List
from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        self.memo = defaultdict(int)

    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        # self.memo = [1] * (length + 1)
        max_ans = 1
        for i in range(1, length):
            max_ans = max(max_ans, self.helper(nums[:i+1]))
        return max_ans

    def helper(self, arr: List[int]) -> int:
        length = len(arr)
        if length == 1:
            return 1

        if self.memo[length] > 1:
            return self.memo[length]

        max_ans = 1
        for i in range(1, length):
            subarr = arr[:i]
            if subarr[-1] < arr[-1]:
                max_ans = max(max_ans, self.helper(subarr) + 1)
        self.memo[length] = max_ans
        return max_ans


print(Solution().lengthOfLIS([5, 2, 1, 4, 3, 1, 6, 9, 4]))
print(Solution().lengthOfLIS([11, 14, 13, 7, 8, 15]))
print(Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
print(Solution().lengthOfLIS([6, 3, 5, 2, 7, 8, 1, 9]))
print(Solution().lengthOfLIS([6, 3, 5, 2, 7, 8, 1]))
