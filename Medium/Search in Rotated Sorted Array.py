"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # binary search approach
        # O(logn) time
        # O(1) space


                
        l, h = 0, len(nums) - 1
        
        while l <= h:
            m = (l + h) // 2
            if target == nums[m]:
                return m
            # left sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target and target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            # right sorted
            else:
                if nums[m] < target and target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
            
        return -1
        
            # l, h, = 0, len(nums) - 1
            
            # while l <= h:
                
            #     m = (l + h) // 2
                
            #     if target == nums[m]:
            #         return m
                
            #     if (nums[l] <= nums[m] and (nums[m] < target or target < nums[l]))\
            #         or (nums[l] > nums[m] and (nums[m] < target and target < nums[l])):
            #         l = m + 1
            #     else:
            #         h = m - 1 
            
            # return -1