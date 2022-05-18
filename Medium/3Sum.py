"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""
from typing import List

# O(n^2) time   O(nlogn) to sort
# O(logn) to O(N) depending on the sorting algorithm
# two pointer method

def threeSum(self, nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []

    nums.sort()
    res = []

    for i in range(len(nums) - 2):
        num = nums[i]
        if num > 0:
            break

        # skip dupilicates
        if i > 0 and num == nums[i - 1]:
            # skip iteration
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            threesum = num + nums[left] + nums[right]
            if threesum == 0:
                res.append([nums[left], nums[right], num])
                left += 1
                right -= 1
                # skip duplicates
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            elif threesum > 0:
                right -= 1
            else:
                left += 1

    return res