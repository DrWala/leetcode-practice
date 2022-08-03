from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ranges = [range(0, 3), range(3, 6), range(6, 9)]
        # length wise check
        for r in range(0, 9):
            nums = set()
            for c in range(0, 9):
                cell = board[r][c]
                if cell == ".":
                    continue
                if cell in nums:
                    return False
                else:
                    nums.add(cell)

        # height wise check
        for r in range(0, 9):
            nums = set()
            for c in range(0, 9):
                cell = board[c][r]
                if cell == ".":
                    continue
                if cell in nums:
                    return False
                else:
                    nums.add(cell)

        # each square check
        for r1 in ranges:
            for r2 in ranges:
                nums = set()
                for r in r1:
                    for c in r2:
                        cell = board[r][c]
                        if cell == ".":
                            continue
                        if cell in nums:
                            return False
                        else:
                            nums.add(cell)
        return True
