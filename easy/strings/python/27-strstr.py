# Unable to solve
# KMP algo
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ctr = 0
        for i in range(len(haystack)):
            if haystack[i] == needle[ctr]:
                ctr += 1
            else:
                ctr = 0
                continue

            if ctr == len(needle):
                return i - len(needle) + 1
        return -1

    # def computeLPSArray(self, pattern):
    #     pattern_length = len(pattern)
    #     len_prev_lps = 0  # length of the previous longest prefix suffix
    #     lps = [0] * pattern_length  # lps[0] is always 0
    #     i = 1

    #     # the loop calculates lps[i] for i = 1 to pattern_length-1
    #     while i < pattern_length:
    #         if pattern[i] == pattern[len_prev_lps]:
    #             len_prev_lps += 1
    #             lps[i] = len_prev_lps
    #             i += 1
    #         else:
    #             # This is tricky. Consider the example.
    #             # AAACAAAA and i = 7. The idea is similar
    #             # to search step.
    #             if len_prev_lps != 0:
    #                 len_prev_lps = lps[len_prev_lps-1]
    #                 # Also, note that we do not increment i here
    #             else:
    #                 lps[i] = 0
    #                 i += 1
    #     return lps


# print(Solution().computeLPSArray("abcabd"))
print(Solution().computeLPSArray("AAACAAAA"))
# 0 1 2 3 4 5 6 7
# A A A C A A A A
# 0 1 2 0 1 2
