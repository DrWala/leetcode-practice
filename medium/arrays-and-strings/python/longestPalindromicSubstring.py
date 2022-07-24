# concept: Expand around center:
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_str = ""
        for i in range(len(s)):
            str_a = self.expand(s, i, i)
            str_b = self.expand(s, i, i + 1)
            local_longest = ""
            if len(str_a) > len(str_b):
                local_longest = str_a
            else:
                local_longest = str_b
            
            if len(local_longest) > len(longest_str):
                longest_str = local_longest
        return longest_str

    def expand(self, s, c1, c2):
        left = c1
        right = c2
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        left += 1
        right -= 1
        
        if left < 0:
            left = 0
        if right >= len(s):
            right = len(s) - 1 
        return s[left:right+1]


print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("a"))
print(Solution().longestPalindrome("ac"))