"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""
from typing import List

# O(n * m * 4^n) time


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        VISITED = 'X'
        m, n, l = len(board), len(board[0]), len(word)
        
        def dfs(r, c, i):
            if i == l:
                return True
            elif -1 < r < m and -1 < c < n and board[r][c] != VISITED and board[r][c] == word[i]:
                i += 1
                tmp = board[r][c]
                board[r][c] = VISITED
                res = dfs(r+1, c, i) or dfs(r-1, c, i) or dfs(r, c+1, i) or dfs(r, c-1, i)
                board[r][c] = tmp
                return res
            else:
                return False
                
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
                
        return False
