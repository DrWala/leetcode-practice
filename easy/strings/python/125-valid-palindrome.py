class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        for i in range(len(s)//2):
            back = len(s) - i - 1
            if s[i] != s[back]:
                return False
        return True

        # Extra pythonic:
        return s == s[::-1]


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("racecar"))
print(Solution().isPalindrome("avani"))
