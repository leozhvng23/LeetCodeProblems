"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sliding window

        if len(s) < len(p) or len(s) == 0 or len(p) == 0:
            return []

        letters = {}
        for i, c in enumerate(p):
            if c not in letters:
                letters[c] = [0, 0]
            letters[c][1] += 1

        res = []
        l = 0

        for i, c in enumerate(s):
            if c in letters:
                letters[c][0] += 1
            if i - l + 1 > len(p):
                if s[l] in letters:
                    letters[s[l]][0] -= 1
                l += 1

            same = True
            for value in letters.values():
                if value[0] != value[1]:
                    same = False
                    break
            if same:
                res.append(l)

        return res
