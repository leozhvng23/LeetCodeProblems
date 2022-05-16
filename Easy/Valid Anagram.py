"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        hm = {}
        for c in s:
            hm[c] = hm[c] + 1 if c in hm else 1
        
        for c in t:
            if c in hm and hm[c] > 0:
                hm[c] -= 1
            else:
                return False
        
        return True 