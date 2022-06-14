"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.
 
Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # DP table-longest common substring
        # O(mn) time
        # O(mn) space
        
        m, n = len(word1), len(word2)
        
        dp = [[0] * (n+1) for _ in range(m+1)]
    
        for r in range(m):
            for c in range(n):
                if word1[r] == word2[c]:
                    dp[r+1][c+1] = dp[r][c] + 1
                else:
                    dp[r+1][c+1] = max(dp[r][c+1], dp[r+1][c])
        
        return (m+n-2*dp[m][n])