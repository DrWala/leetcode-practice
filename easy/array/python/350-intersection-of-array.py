from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        ctr = Counter(nums1)
        ans = []
        for n in nums2:
            if n in ctr:
                ans.append(n)
                ctr[n] -= 1
        return ans
