# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        my original solution

        if len(inorder) == 1:
            root = TreeNode(inorder[0])
            return root

        val = postorder[-1]
        parent = TreeNode(val)

        # find parent node location in inorder

        leftNodes = 0
        for i in inorder:
            if i == val:
                break
            leftNodes += 1

        rightNodes = len(inorder) - leftNodes - 1
        if leftNodes > 0:
            parent.left = self.buildTree(inorder[:leftNodes], postorder[:leftNodes])
        if rightNodes > 0:
            parent.right = self.buildTree(inorder[-rightNodes:], postorder[-1-rightNodes:-1])

        return parent
        """



        """
        # cleaner version: O(n^2) solution
        
        def rec(inorder, postorder):
            # base condition
            if not inorder or not postorder:
                return
            root = TreeNode(postorder.pop())
            mid = inorder.index(root.val)
            root.right = rec(inorder[mid+1:], postorder)
            root.left = rec(inorder[:mid], postorder)
            return root

        return rec(inorder, postorder)
        """

        # Optimized Version O(n)

        mapper = {}

        for i, v in enumerate(inorder):
            mapper[v] = i

        def rec(low, high):
            # base condition
            if low > high:
                return

            root = TreeNode(postorder.pop())
            mid = mapper[root.val]
            root.right = rec(mid + 1, high)
            root.left = rec(low, mid - 1)
            return root

        return rec(0, len(inorder) - 1)

