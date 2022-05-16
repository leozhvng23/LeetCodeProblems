"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        if len(strs) <= 1:
            return [strs]

        hm, ans = {}, []
        for word in strs: # n times
            sorted_str = "".join(sorted(word)) # O(klogk) k: max len of word
            if sorted_str in hm:
                idx = hm[sorted_str]
                ans[idx].append(word)
            else:
                hm[sorted_str] = len(ans)
                ans.append([word])
        
        return ans
        """
        

        # categorize by sorted string
        # O(nklogk)
        # space: O(nk)
        """ 
        hm = defaultdict(list)
        for word in strs:
            hm["".join(sorted(word))].append(word)
        
        return hm.values()

        """


        # Time: O(NK)
        # Space: O(NK)

        hm = defaultdict(list)
        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord('a')] += 1
            hm[tuple(count)].append(w)
            
        return hm.values()
        


        
