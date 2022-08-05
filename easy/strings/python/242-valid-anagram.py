from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("cat", "rat"))
