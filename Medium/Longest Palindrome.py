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
    if len(s) <= 1:
        return s

    same = True
    for i in s:
        if i != s[0]:
            same = False
    if same:
        return s

    i, left, right, last = 0, 0, 0, None

    for i in range(len(s)):
        l, r = i, i
        while l > -1 and r < len(s):
            if s[l] != s[r]:
                break
            if r - l + 1 > right - left + 1:
                left, right = l, r
            l, r = l - 1, r + 1
        if s[i] == last:
            l, r = i - 1, i
            # same while loop as above
            while l > -1 and r < len(s):
                if s[l] != s[r]:
                    break
                if r - l + 1 > right - left + 1:
                    left, right = l, r
                l, r = l - 1, r + 1
        last = s[i]

    return s[left: right + 1]