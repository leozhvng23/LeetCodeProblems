
"""
------------------------------
Single Element in a Sorted Array
------------------------------

Given a sorted array consisting of only integers where
every element appears twice except for one element which appears once.
Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
"""
from typing import List


def single_element_in_sorted_array(nums: List[int]) -> int:
    """
    # sliding window: Time: O(n)
    for i in range(0, len(arr), 2):
        if i + 1 > len(arr) - 1:
            return arr[i]
        elif arr[i] != arr[i+1]:
            return arr[i]
    """

    # binary search: Time: O(log(n))

    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if (high - mid) % 2 > 0:  # odd
            if nums[mid-1] == nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        else:  # even, flip directions
            if nums[mid-1] == nums[mid]:
                high = mid
            else:
                low = mid

    return nums[low]


arr = [1, 1, 2, 2, 3, 3, 4]
arr2 = [1, 1, 2, 2, 3]
arr3 = [3, 3, 7, 7, 10, 11, 11]
arr4 = [1, 1, 2, 3, 3]
arr5 = [1]
arr6 = [1, 1, 2, 3, 3]

print(single_element_in_sorted_array(arr))
print(single_element_in_sorted_array(arr2))
print(single_element_in_sorted_array(arr3))
print(single_element_in_sorted_array(arr4))
print(single_element_in_sorted_array(arr5))
print(single_element_in_sorted_array(arr6))

