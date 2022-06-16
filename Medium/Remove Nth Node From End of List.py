"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
"""
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        ct, l, r = 0, None, head.next
        
        while r:
            if ct == n-1:
                l = head if not l else l.next
            else:
                ct += 1
            r = r.next
            
        if not l:
            return head.next
        
        l.next = l.next.next
        
        return head