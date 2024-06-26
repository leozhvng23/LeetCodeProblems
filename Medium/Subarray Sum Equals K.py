from typing import List

"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cur_sum, res = 0, 0
        hm = {0: 1}

        for num in nums:
            cur_sum += num
            if cur_sum - k in hm:
                res += hm[cur_sum - k]
            hm[cur_sum] = hm.get(cur_sum, 0) + 1

        return res
