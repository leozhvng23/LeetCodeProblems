from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bottom up recursion
        def recursiveMaxDepth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return max(recursiveMaxDepth(node.left), recursiveMaxDepth(node.right)) + 1

        return recursiveMaxDepth(root)
