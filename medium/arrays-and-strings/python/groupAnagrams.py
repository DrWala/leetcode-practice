from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Concept: hash each anagram and assign it a group
        anagram_map = defaultdict(list)
        for anagram in strs:
            sorted_anagram = "".join(sorted(anagram))
            anagram_map[sorted_anagram].append(anagram)
        
        return list(anagram_map.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))

strs = [""]
print(Solution().groupAnagrams(strs))

strs = ["a"]
print(Solution().groupAnagrams(strs))
