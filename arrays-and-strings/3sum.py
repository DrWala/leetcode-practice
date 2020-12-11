from collections import Counter

class Solution(object):
    def twoSum(self, nums, target):
        num_list = nums
        num_set = Counter(nums)
        ret = []
        for num in num_list:
            num_set[num] -= 1
            if target - num in num_set and num_set[target - num] != 0:
                ret.append(sorted([num, target - num, -1 * target]))
            num_set[num] += 1
        return ret
    
    def threeSum(self, nums):
        ret = set()
        nums = sorted(nums)
        for idx, num in enumerate(nums):
            res = self.twoSum(nums[:idx] + nums[idx + 1:], -1 * num)
            if res is not None:
                for two_sum in res:
                    ret.add(tuple(two_sum))
        return [list(i) for i in ret]

print(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0, 0, 0]))