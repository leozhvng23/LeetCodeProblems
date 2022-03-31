from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def compare(left_node: [TreeNode], right_node: [TreeNode]) -> bool:
            if not left_node or not right_node:
                return left_node == right_node

            return left_node.val == right_node.val \
                   and compare(left_node.left, right_node.right) \
                   and compare(left_node.right, right_node.left)

        if not root:
            return True
        return compare(root.left, root.right)

