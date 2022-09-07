"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        S, T = {}, {}
        for i, j in zip(s, t):
            if i not in S and j not in T:
                S[i], T[j] = j, i
            elif S.get(i) != j or T.get(j) != i:
                return False 
        return True