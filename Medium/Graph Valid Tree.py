"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
Return true if the edges of the given graph make up a valid tree, and false otherwise.

Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
"""
from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # classic cycle detection in undirected graph
        # O(|V| + |E|) time
        # O(|V| + |E|) space
        
        G = defaultdict(list)
        
        for v in edges:
            G[v[0]].append(v[1])
            G[v[1]].append(v[0])
            
        visit = set()
        
        # use parent to negate trivial cycles like A <==> B
        
        def isCycle(node, parent):
            if node in visit:
                return True
            visit.add(node)
            for neighbor in G[node]:
                if neighbor == parent:
                    continue
                if isCycle(neighbor, node):
                    return True
            return False

        # for a graph to be a tree all nodes have to be connected
        # run dfs from one node and check if it reaches all nodes
        
        return not isCycle(0, -1) and n == len(visit)
            
        
            
        