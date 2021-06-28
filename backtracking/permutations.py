class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        perms = []
        perms.append([])

        for num in nums:
            res = []
            for perm in perms:
                res.extend(self.insert(num, perm))
            perms = res
        return perms

    def insert(self, num, perm: List[int]):
        if len(perm) == 0:
            perm = [[num]]
            return perm
        else:
            lengthNewArr = len(perm) + 1
            perms = self.deep_copy_repeat(perm, lengthNewArr)
            idx = 0
            for perm in perms:
                perm.insert(idx, num)
                idx += 1
            return perms

    def deep_copy_repeat(self, lst: List[int], times: int):
        res = []
        for j in range(times):
            res.append([i for i in lst])
        return res
