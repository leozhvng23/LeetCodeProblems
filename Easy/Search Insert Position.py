"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""


def searchInsert(self, nums: List[int], target: int) -> int:

    # binary search O(log n)

    l, h, mid = 0, len(nums) - 1, 0

    while l <= h:
        mid = (l + h) // 2
        if target < nums[mid]:
            h = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else:
            return mid

    if target > nums[mid]:
        return mid + 1
    return mid

