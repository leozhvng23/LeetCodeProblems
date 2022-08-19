"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
"""
from typing import List


"""
Time Complexity: O(n^2) We have outer and inner loops, each going through n elements.

Sorting the array takes O(nlogn), so overall complexity is O(nlogn+n^2) 
This is asymptotically equivalent to O(n^2) 

Space Complexity: from O(logn) to O(n), depending on the implementation of the sorting algorithm.


"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closestSum = float('inf')
        for i, v in enumerate(nums):
            l, r = i+1, n-1
            while l < r:
                s = nums[l] + nums[r] + v
                if abs(s - target) < abs(target-closestSum):
                    closestSum = s
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return s

        return closestSum
