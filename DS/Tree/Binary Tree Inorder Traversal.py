from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative

        stack = []
        res = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                curr = stack.pop()
                res.append(curr.val)
                root = curr.right

        return res


