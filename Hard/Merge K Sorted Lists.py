"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge sort
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged = []
            if len(lists) % 2 == 1:
                lists.append(None)
            for i in range(0, len(lists), 2):
                merged.append(self.merge(lists[i], lists[i + 1]))    
            lists = merged
        
        return lists[0]
        
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2, prev = list1, list2, ListNode()
        head = prev
        while l1 and l2:
            if l2.val < l1.val:
                prev.next = l2
                l2 = l2.next
            else:
                prev.next = l1       
                l1 = l1.next
            prev = prev.next
            
        prev.next = l1 or l2
        
        return head.next
        