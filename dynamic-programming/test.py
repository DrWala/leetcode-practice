from collections import defaultdict
from operator import ne
from typing import List, Tuple
import math

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        src_r, src_c, dest_r, dest_c  = self.get_src_dest(matrix)
        src = (src_r, src_c)
        dest = (dest_r, dest_c)

        return self.helper(src, dest, matrix)

        
    def get_src_dest(self, matrix:  List[List[int]]) -> Tuple[int, int, int, int]:
        rows = len(matrix)
        cols = len(matrix[0])
        min_val, max_val, min_r, min_c, max_r, max_c = math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf
        
        for i in range(rows):
            for j in range(cols):
                # Coordinates of min/max
                if min_val > matrix[i][j]:
                    min_r = i
                    min_c = j
                    min_val = matrix[i][j]
                
                if max_val < matrix[i][j]:
                    max_r = i
                    max_c = j
                    max_val = matrix[i][j]

        return min_r, min_c, max_r, max_c
    
    def get_neighbours(self, src: Tuple[int], matrix:  List[List[int]]) -> Tuple[Tuple[int]]:
        directions = [[0,1], [1,0], [1,1], [1, 0]]
        rows = len(matrix)
        cols = len(matrix[0])
        curr = matrix[i][j]
        i, j = src
        neighbours = []

        for di, dj in directions:
            offset_i = i + di
            offset_j = j + dj 
            
            # Bounds checking
            if 0 < offset_i < rows and  0 < offset_j < cols:
                neighbour = matrix[offset_i][offset_j]
                if neighbour > curr:
                    neighbours.append((offset_i, offset_j))
        
        return neighbours

    
    def helper(self, src: Tuple[int, int], dest: Tuple[int, int], graph: List[List[int]]):
        dp = defaultdict(int)
        dp[tuple(dest)] = 0

        def longest_path(src: Tuple[int, int], dest: Tuple[int, int], graph: List[List[int]]) -> int:
            if src == dest:
                return dp[dest]
            else:
                if dp[src] != -1:
                    return dp[src]
                else:
                    longest_neighbour_path = -1
                    for neighbour in self.get_neighbours((i,j), graph):
                        longest_neighbour_path = max(longest_neighbour_path, longest_path(graph, neighbour, dest))
                    dp[src] = longest_neighbour_path + 1
                    return dp[src]

        return longest_path(graph, src, dest)

matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(Solution().longestIncreasingPath(matrix))
