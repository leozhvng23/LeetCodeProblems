"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """
    # brute force
    hashmap = {}
    i, j, s = 0, 0, 0

    length = len(nums1) + len(nums2)
    if length % 2 > 0:
        mid = (length + 1) // 2
    else:
        mid = length // 2

    while i < len(nums1) and s <= mid:
        if j < len(nums2):
            if nums2[j] > nums1[i]:
                hashmap[s] = nums1[i]
                i += 1
            elif nums2[j] <= nums1[i]:
                hashmap[s] = nums2[j]
                j += 1
        else:
            hashmap[s] = nums1[i]
            i += 1
        s += 1

    while j < len(nums2) and s <= mid:
        hashmap[s] = nums2[j]
        s += 1
        j += 1

    if s == 1:
        return hashmap[s - 1]
    elif length % 2 > 0:
        return hashmap[s - 2]
    else:
        return (hashmap[s - 1] + hashmap[s - 2]) / 2
    """

    # binary search
    l1 = 0
    h1 = len(nums1) - 1

    l2 = 0
    h2 = len(nums2) - 1

    # while l1




print(findMedianSortedArrays([1, 2, 3], [1, 3, 6]))

