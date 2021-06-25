from typing import List
import queue


class Solution:
    visited = []
    count = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        # Reset instance variables as the method will be reused during grading
        self.visited = []
        self.count = 0

        # Set up unvisited grid
        for row in grid:
            unvisited_row = [0 for point in row]
            self.visited.append(unvisited_row)

        # Go through every single point. If we find an unvisited piece of land, find all its
        # neighbours and mark them with the current count
        for r, row in enumerate(grid):
            for c, point in enumerate(row):
                if grid[r][c] == "1" and self.visited[r][c] == 0:
                    self.count += 1
                    self.mark_islands(r, c, grid)
        return self.count

    def mark_islands(self, r, c, grid):
        max_col_idx = len(grid[0]) - 1
        max_row_idx = len(grid) - 1

        # We will use a simple BFS to find all the islands connected to this point
        points = []
        points.append((r, c))

        self.visited[r][c] = self.count

        while len(points) > 0:
            r, c = points.pop()
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for move in moves:
                r_check = r + move[0]
                c_check = c + move[1]

                # Check if the neighbour is out of bounds
                out_of_bounds = r_check < 0 or r_check > max_row_idx or c_check < 0 or c_check > max_col_idx

                # If the point is not out of bounds, is land, and has not been visited yet, we mark it as visited
                if not out_of_bounds and grid[r_check][c_check] == "1" and self.visited[r_check][c_check] == 0:
                    self.visited[r_check][c_check] = self.count
                    points.append((r_check, c_check))


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(Solution().numIslands(grid))
