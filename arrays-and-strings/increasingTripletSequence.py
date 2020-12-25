class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float("inf")
        second = float("inf")
        for num in nums:
            if num < first:
                first = num
            if num > first:
                second = min(num, second)
            if num > second:
                return True
        return False
            
# print(Solution().increasingTriplet([1,2,3,4,5]))
# print(Solution().increasingTriplet([5,4,3,2,1]))
# print(Solution().increasingTriplet([2,1,5,0,4,6]))
print(Solution().increasingTriplet([20,100,10,12,5,13]))