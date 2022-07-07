"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from typing import List

# O(M*N) time 
# O(M*N) space

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        VISITED, M, N, res = 'X', len(grid), len(grid[0]), 0
        
        def dfs(r, c):
            if (r not in range(M) or c not in range(N) or
                grid[r][c] == VISITED or grid[r][c] == "0"):
                return
            else:
                grid[r][c] = VISITED
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for i, j in directions:
                    dfs(r + i, c + j)
        
        for r in range(M):
            for c in range(N):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        
        return res
                    