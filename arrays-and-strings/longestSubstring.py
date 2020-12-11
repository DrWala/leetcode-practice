class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = s
        char_set = set()
        i, j = 0, 0
        max = 0
        while j < len(chars):
            if chars[j] not in char_set:
                char_set.add(chars[j])
                j += 1
            else:
                set_length = len(char_set)
                max = set_length if set_length > max else max
                char_set.remove(chars[i])
                i += 1
        # We have this check because there is a chance that the longest substring is
        # the last thing the program checks. Max won't be updated at that point. So the
        # source of truth will be char_set and not max.
        set_length = len(char_set)
        return max if max > set_length else set_length

s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))

s = ""
print(Solution().lengthOfLongestSubstring(s))

s = " "
print(Solution().lengthOfLongestSubstring(s))
