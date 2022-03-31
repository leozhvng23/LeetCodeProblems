from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = deque()
        res = []

        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.right
            else:
                node = stack.pop()
                root = node.left

        # return in reverse order
        return res[::-1]

