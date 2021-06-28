class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        else:
            res = []
            res.append([])
            for num in nums:
                dup = self.deep_copy_2layer(res)
                for sub in dup:
                    sub.append(num)
                res.extend(dup)
            return res

    def deep_copy_2layer(self, listoflists: List[List[int]]):
        res = []
        for arr in listoflists:
            res.append([i for i in arr])
        return res
