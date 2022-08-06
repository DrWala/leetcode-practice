from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: Empty array
        if (len(strs) == 0):
            return ""

        col = 0
        shortest_str = min([len(s) for s in strs])

        # Edge case: we have "" in the array, longest prefix is ""
        if shortest_str == 0:
            return ""

        # We only iterate as far as the shortest string
        for col in range(shortest_str):
            all_same = True
            first = strs[0][col]
            for row in range(len(strs)):
                all_same = first == strs[row][col] and all_same
                if not all_same:
                    return strs[0][:col]
        return strs[0][:shortest_str]


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(["flo", "flower", "flow", "flight"]))
print(Solution().longestCommonPrefix([""]))
print(Solution().longestCommonPrefix([]))
print(Solution().longestCommonPrefix(["a"]))
