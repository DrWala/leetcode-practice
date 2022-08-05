from typing import List
from collections import Counter


class Solution(object):
    def firstUniqChar(self, s) -> int:

        ctr = Counter(s)
        relevant = [(k, v) for k, v in ctr.most_common() if v == 1]
        if (len(relevant)) == 0:
            return -1
        first = relevant[0][0]
        return s.index(first)

        # Thought this would be faster, but apparently not
        # freq = {}
        # for idx, c in enumerate(s):
        #     if c in freq:
        #         freq[c][0] += 1
        #         freq[c][1] = idx
        #     else:
        #         freq[c] = [1, idx]

        # for k, v in freq.items():
        #     count, idx = v
        #     if count == 1:
        #         return idx
        # return -1


print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar("aabb"))
