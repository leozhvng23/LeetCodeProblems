"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
from typing import List
    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(N) time
        # O(N) space
        
        hm = set(nums)
        longest = 0
        for v in hm:
            if v-1 not in hm: # starting number
                cur, l = v, 1
                while cur+1 in hm:
                    l += 1
                    cur += 1
                longest = max(longest, l)
        
        return longest

        

