"""
You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.
Return the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:
Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:

Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.
"""
from typing import Optional


# DFS 
# O(N) time
# O(H) space, where H is the height of the tree 


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        covered = {None}
        self.cameras = 0
    
        def dfs(node: Optional[TreeNode], parent = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                if (not parent and node not in covered) or (node.left not in covered or node.right not in covered):
                    self.cameras += 1
                    covered.update({node, node.left, node.right, parent})

        dfs(root)
        
        return self.cameras
        
    
                    
        
            
                
            
                
        
        