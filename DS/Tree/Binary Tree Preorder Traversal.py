# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """ Iterative 1"""
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        stack = deque()
        stack.append(root)
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res

    """ Iterative 2"""

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque()
        res = []

        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            else:
                node = stack.pop()
                root = node.right

        return res

    """ Recursive """

    def recursivePreorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def recursiveTraverse(node: Optional[TreeNode]):
            if not node:
                return []
            return [node.val] + recursiveTraverse(node.left) + recursiveTraverse(node.right)

        return recursiveTraverse(root)


