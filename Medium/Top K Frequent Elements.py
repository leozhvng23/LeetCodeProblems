"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

import heapq as hq
from re import L
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # O(nlogk) time complexity
        # Time analysis for heapq.nlargest():
        # For building the heap for first t elements will be done tlog(t)
        # For pushing and popping, the remaining elements will be done in (n-t)log(t)
        # The overall time complexity will be nlog(t)
        # Space: O(N)

        """

        hm = {}
        for v in nums:
            hm[v] = hm[v] + 1 if v in hm else 1

        res = hq.nlargest(k, [(val, key) for key, val in hm.items()])

        return [v[1] for v in res]

        """
        
        """
        # Uses sort
        # O(nlogn) time complexity

        hm = {}
        for v in nums:
            hm[v] = hm[v] + 1 if v in hm else 1
            
        hm = list(hm.items())
        hm.sort(key = lambda x: -x[1])

        return [v[0] for v in hm[:k]]
        """

        # Bucket Sort 
        # O(N) time
        # O(N) space

        hm = {}
        for v in nums:
            hm[v] = 1 + hm.get(v, 0)

        freq = [[] for _ in range(len(nums) + 1)]

        for n, f in hm.items():
            freq[f].append(n)

        res = []

        for v in freq[::-1]:
            for j in v:
                res.append(j)
                if len(res) == k:
                    return res
        