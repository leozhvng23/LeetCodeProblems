"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
Return the number of connected components in the graph.

Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
"""


from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        G = defaultdict(list)
        
        for v in edges:
            G[v[0]].append(v[1])
            G[v[1]].append(v[0])
            
        visited = set()
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in G[node]:
                dfs(neighbor)
        
        res = 0 
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
                
        return res