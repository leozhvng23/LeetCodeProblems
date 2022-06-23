"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
 
Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        # pre-order traversal
        # '*' for Null values
        
        def dfs(node):
            if not node:
                return '*,'
            return str(node.val) + ',' + dfs(node.left) + dfs(node.right)
        
        return dfs(root)

    def deserialize(self, data):

        arr = deque(data.split(','))
        
        def dfs(arr):
            cur = arr.popleft()
            if cur == '*':
                return None
            return TreeNode(cur, dfs(arr), dfs(arr))
            
        return dfs(arr)
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))