"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

1---3---1
        |
1   5   1
        |
4   2   1

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # use given matrix as in-place dp table

        m = len(grid)
        n = len(grid[0])

        # init boundary
        for i in range(1, m):
            grid[i][0] = grid[i - 1][0] + grid[i][0]

        for j in range(1, n):
            grid[0][j] = grid[0][j - 1] + grid[0][j]

        # O(mn) iterate through table

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min((grid[i][j] + grid[i - 1][j]), (grid[i][j] + grid[i][j - 1]))

        return grid[m - 1][n - 1]