from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i, row in enumerate(matrix):
            for j in range(len(row) // 2):
                other = len(row) - j - 1
                row[j], row[other] = row[other], row[j]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Solution().rotate(matrix)
print(matrix)
