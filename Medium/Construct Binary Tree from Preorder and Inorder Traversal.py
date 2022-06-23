"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # O(N) time
        # O(N) space
        
        hm = {v: i for i, v in enumerate(inorder)}
        self.idx = 0
        
        def buildTree(left, right):
            if left == right:
                return None
            
            root_val = preorder[self.idx]
            self.idx += 1
            split = hm[root_val]
            
            return TreeNode(root_val, buildTree(left, split), buildTree(split + 1, right))
        
        return buildTree(0, len(preorder))