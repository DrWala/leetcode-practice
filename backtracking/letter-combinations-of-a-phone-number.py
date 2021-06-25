from typing import List
import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        numberCharMap = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        digits = [int(d) for d in list(digits)]
        lists = list(map(lambda d: numberCharMap[d], (digits)))
        cartesian_list = list(itertools.product(*lists))
        cartesian_list = map(lambda t: "".join(t), cartesian_list)
        return list(cartesian_list)


print(Solution().letterCombinations("23"))
