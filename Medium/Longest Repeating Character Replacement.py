"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        # sliding window approach
        # hashmap to keep track of frequency of appearance
        # O(N) time complexity
        # O(1) space, storing only 26 letters
        
        hm = {}
        
        l, maxl, maxf = 0, 0, 0
            
        for r,v in enumerate(s):
            hm[v] = hm.get(v, 0) + 1
            maxf = max(maxf, hm[v])
            
            if (r-l+1) - maxf > k:
                hm[s[l]] -= 1
                l += 1
                   
            maxl = max(maxl, r - l + 1)            
            
        return maxl

