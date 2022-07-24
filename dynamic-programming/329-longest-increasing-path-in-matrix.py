from collections import defaultdict
from typing import List
import math

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        graph, src_r, src_c, dest_r, dest_c  = self.convert_to_adj_list(matrix)
        
        

        
    def convert_to_adj_list(self, matrix:  List[List[int]]) -> tuple(dict, int, int, int, int): 
        directions = [[0,1], [1,0], [1,1], [1, 0]]
        rows = len(matrix)
        cols = len(matrix[0])
        graph = defaultdict(list)
        min_val, max_val, min_r, min_c, max_r, max_c = -math.inf, math.inf, -math.inf, -math.inf, -math.inf, -math.inf
        
        for i in range(rows):
            for j in range(cols):
                # Coordinates of min/max
                if min_val > min(matrix[i][j], min_val):
                    min_r = i
                    min_j = j
                    min_val = matrix[i][j]
                
                if max_val < max(matrix[i][j], max_val):
                    max_r = i
                    max_j = j
                    max_val = matrix[i][j]
                
                for di, dj in directions:
                    offset_i = i + di
                    offset_j = j + dj 
                    # Bounds checking
                    if 0 < offset_i < rows and  0 < offset_j < cols:
                        neighbour = matrix[offset_i][offset_j]
                        curr = matrix[i][j]
                        if neighbour > curr:
                            graph[str(curr)].append(str(neighbour))
        
        return graph, min_r, min_c, max_r, max_c

    def helper(src: str, dest: str, graph: dict):
        dp = [-1] * len(graph)
        dp[4] = 0

    def longest_path(graph: dict, src: int, dest: int) -> int:
        if src == dest:
            return dp[dest]
        else:
            if dp[src] != -1:
                return dp[src]
            else:
                longest_neighbour_path = -1
                for neighbour in graph[src]:
                    longest_neighbour_path = max(longest_neighbour_path, longest_path(graph, neighbour, dest))
                dp[src] = longest_neighbour_path + 1
                return dp[src]

    print(longest_path(graph, 0, 4))
