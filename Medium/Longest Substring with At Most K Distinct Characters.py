"""
Given a string s and an integer k, return the length of the longest substring of s that contains 
at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
"""
from collections import OrderedDict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # sliding window
        # O(N) time
        # O(N) space

        if k == 0:
            return 0

        # use OrderedDict to always get the leftmost unique value
        hm = OrderedDict()
        l, longest = -1, 0

        for r, v in enumerate(s):
            if v in hm:
                # delete so after insert its the rightmost item in hm
                # so we can update the order in hm
                hm.pop(v)
            if len(hm) == k and v not in hm:
                # delete left most unique value
                _, index = hm.popitem(last=False)
                l = index
            hm[v] = r
            longest = max(longest, r - l)

        return longest
