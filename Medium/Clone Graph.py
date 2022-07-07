"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
"""

from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        # traverse with BFS and build new graph as we go

        visited = {}
        q = deque([node])  # make queue and append root
        visited[node] = Node(node.val)  # root is visited

        while q:
            new_node = q.popleft()
            for n in new_node.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val)  # add to visited and store clone node
                    q.append(n)
                # add old neighbors to the new clone node's neighbors list
                visited[n].neighbors.append(visited[new_node])

        return visited[node]

    """
    # recursive DFS approach
    
    def cloneGraph(self, node):

        visited = {}

        def dfs(root):
            if root in visited:
                 return visited[root]
            else:
                cloneNode = Node(root.val)
                visited[root] = cloneNode
                cloneNode.neighbors = [dfs(n) for n in root.neighbors]
                return cloneNode
        
        return dfs(node) if node else None
             
  
    """

