"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        count, longest = 0, 0
        hm = {0: -1}
        for i, c in enumerate(nums):
            count = count + 1 if c == 1 else count - 1
            if count in hm:
                longest = max(longest, i - hm[count])
            else:
                hm[count] = i

        return longest