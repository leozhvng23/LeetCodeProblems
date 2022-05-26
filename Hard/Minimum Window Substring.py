"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # sliding window
        # O(m + n) time
        # O(m + n) space, two hash tables for 52 upper and lower case letters
        
        ct, fr = {}, {}
        for v in t:
            ct[v] = ct.get(v, 0) + 1 # reference table for count
            fr[v] = 0 # keeps track of current count
            
        low, high, l, n, k = 0, float('inf'), float('inf'), len(ct), 0
        
        for r, v in enumerate(s):
            if v in fr:
                l = min(l, r) # initialize l
                fr[v] += 1
                if fr[v] == ct[v]:
                    k += 1 # all counts of this letter present in window
                    
                if k == n: # all letters present in window
                    while True: # trim letters in the front
                        if s[l] in fr:
                            if fr[s[l]] > ct[s[l]]:
                                fr[s[l]] -= 1
                            else:
                                break
                        l += 1
                        
                    if r-l + 1 < high - low + 1:
                        low, high = l, r
                     
        return s[low:high + 1] if high != float('inf') else ""
            