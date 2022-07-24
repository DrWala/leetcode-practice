from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)

        # not sure why this works
        if k == len(nums):
            return nums

        # My old answer
        # invCounter = [[v, k] for k, v in ctr.items()]
        # mostFreqTuples = sorted(
        #     invCounter, reverse=True, key=lambda x: x[0])[0: k]
        # return [t[1] for t in mostFreqTuples]

        return heapq.nlargest(k, ctr.keys(), key=ctr.get)


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(Solution().topKFrequent([1], 1))
print(Solution().topKFrequent([1, 2], 2))
