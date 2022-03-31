"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
"""

from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # construct graph
        G = defaultdict(list)
        for e in prerequisites:
            src, dst = e[0], e[1]
            G[src].append(dst)

        # topo sort using dfs
        white, gray, black = 0, -1, 1
        status = [0] * numCourses
        topo_order = []

        def isCycle(u):
            if status[u] == white:
                # unvisited
                status[u] = gray
                for v in G[u]:
                    if isCycle(v):
                        return True
                status[u] = black
                topo_order.append(u)  # append finished u
                return False
            elif status[u] == gray:
                # cycle!
                return True
            else:
                # visited
                return False

        for u in range(numCourses):
            if isCycle(u):
                return []

        return topo_order






