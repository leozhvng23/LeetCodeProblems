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
            # traverse down to left most node
            while root:
                stack.append(root)
                root = root.left
                
            # traverse up to parent
            curr = stack.pop()
            res.append(curr.val)

            # advance to right child
            root = curr.right

        return res


