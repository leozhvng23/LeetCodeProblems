"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

def longestPalindrome(self, s: str) -> str:
    # O(N^2) time
        # O(1) space
    
        res, n = "", len(s)
        
        if n <= 1:
            return s
        
        for i in range(n):
            for r in range(i, i+2): # executes twice
                l = i
                while l > -1 and r < n and s[l] == s[r]:
                    l, r = l - 1, r + 1
                if r - l - 1 > len(res):
                    res = s[l+ 1:r]
        
        return res