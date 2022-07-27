from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ptr = len(digits) - 1
        while ptr >= 0:
            if digits[ptr] != 9:
                digits[ptr] += 1
                return digits
            else:
                digits[ptr] = 0
                ptr -= 1
        # This is the case where the number is like 99, we need to add a digit.
        # We set the first digit to 1 and add a 0 to the back, instead of prepending a 1
        digits[0] = 1
        digits.append(0)
        return digits


print(Solution().plusOne([1, 2, 3]))
print(Solution().plusOne([4, 3, 2, 1]))
print(Solution().plusOne([2, 9]))
print(Solution().plusOne([9]))
print(Solution().plusOne([9, 9]))
