from collections import defaultdict
from typing import List, Tuple


class Solution:
    def __init__(self):
        self.memo = []

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            self.memo.append([0] * cols)

        longest_path = 0

        for i in range(rows):
            for j in range(cols):
                longest_path = max(
                    longest_path, self.dfs_count((i, j), matrix, rows, cols))

        return longest_path + 1

    def get_neighbours(self, src: Tuple[int], matrix:  List[List[int]], rows: int, cols: int) -> Tuple[Tuple[int]]:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        i, j = src
        curr = matrix[i][j]
        neighbours = []

        for di, dj in directions:
            offset_i = i + di
            offset_j = j + dj

            # Bounds checking
            if 0 <= offset_i < rows and 0 <= offset_j < cols:
                neighbour = matrix[offset_i][offset_j]
                if neighbour > curr:
                    neighbours.append((offset_i, offset_j))

        return neighbours

    def dfs_count(self, src: Tuple[int, int], graph: List[List[int]], rows: int, cols: int) -> int:
        i, j = src
        if self.memo[i][j] != 0:
            return self.memo[i][j]

        max_len = 0
        neighbours = self.get_neighbours(src, graph, rows, cols)
        for n in neighbours:
            max_len = max(max_len, 1 + self.dfs_count(n, graph, rows, cols))

        self.memo[i][j] = max_len
        return max_len


matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
print(Solution().longestIncreasingPath(matrix))

matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
print(Solution().longestIncreasingPath(matrix))

matrix = [[1]]
print(Solution().longestIncreasingPath(matrix))

matrix = [[7, 6, 1, 1],
          [2, 7, 6, 0],
          [1, 3, 5, 1],
          [6, 6, 3, 2]]
print(Solution().longestIncreasingPath(matrix))
