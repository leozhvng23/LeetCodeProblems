"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        hashmap = {}
        length = 0
        i = 0

        while i < len(s):
            if s[i] in hashmap:
                new_length = len(hashmap)
                if new_length > length:
                    length = new_length
                s = s[hashmap[s[i]] + 1:]
                hashmap = {}
                i = 0
            else:
                hashmap[s[i]] = i
                i += 1

        if len(hashmap) > length:
            return len(hashmap)
        else:
            return length
        """

        # sliding window solution using hashmap

        hashmap = {}
        left = 0
        length = 0

        for right, char in enumerate(s):
            if char in hashmap:
                left = max(hashmap[char] + 1, left)
            hashmap[char] = right
            length = max(right - left + 1, length)

        return length
