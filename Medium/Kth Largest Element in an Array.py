"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
 
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap O(nlogk) time
        # here we use quick select which has an average run time of O(n)
        # O(1) space
        
        def quickSelect(left: int, right: int):
            # list contains only one element
            if left == right:
                return nums[left]
            
            # pick random pivot
            pivot_idx = random.randint(left, right)
            
            # move pivot to the end
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            
            # partition array
            split = partition(left, right)
            kth = len(nums) - split
            
            if kth == k:
                return nums[split]
            elif kth > k:
                return quickSelect(split + 1, right)
            else:
                return quickSelect(left, split - 1)
            
        
        def partition(left: int, right: int): 
            pivot, split = nums[right], left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[split] = nums[split], nums[i]
                    split += 1
            # swap pivot and split
            nums[right], nums[split] = nums[split], nums[right]

            return split
        
        return quickSelect(0, len(nums) - 1)
        