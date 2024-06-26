"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # O(N) time
        # O(N) space (excluding output array)
        """
        n = len(nums)
        left = [1] * (n + 1)
        right = [1] * (n + 1)

        for i in range(1, n + 1):
            left[i] = left[i - 1] * nums[i - 1]
            right[-i - 1] = right[-i] * nums[-i]

        ans = [left[i] * right[i + 1] for i in range(n)]
        return ans
        """

        # O(N) time
        # O(1) space (excluding output array)

        n = len(nums)
  
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        
        p = 1
        for i in range(n-1, -1, -1):
            res[i] *= p
            p *= nums[i]
            
        return res