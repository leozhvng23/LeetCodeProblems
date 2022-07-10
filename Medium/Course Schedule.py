"""
207. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct a graph

        graph = defaultdict(list)
        for e in prerequisites:
            graph[e[0]].append(e[1])

        print(graph)

        status = [0] * numCourses

        # -1: visiting, 0: unvisited, 1: visiting

        def iscycle(u):
            # unvisited
            if status[u] == 0:
                status[u] = -1  # set to visiting
                for v in graph[u]:
                    if iscycle(v):
                        return True
                status[u] = 1  # set to visited
                return False

            # visited
            elif status[u] == 1:
                return False

            # visiting
            elif status[u] == -1:
                # visiting, cycle!
                return True

        for u in range(numCourses):
            if iscycle(u):
                return False
        return True


        """
        UNVISITED, VISITING, VISITED = 0, -1, 1

        G = defaultdict(list)
        for course in prerequisites:
            G[course[0]].append(course[1])
            
        status = [UNVISITED for _ in range(numCourses)]

        def isCycle(course):
            if status[course] == VISITING:
                return True
            if status[course] == VISITED:
                return False
            
            status[course] = VISITING
            for prereq in G[course]:
                if isCycle(prereq):
                    return True
            status[course] = VISITED
            
            return False
        
        for course in range(numCourses):
            if isCycle(course):
                return False
            
        return True
        
        """


"""
basically this problem asks us to find if there are any cycles in the graph
to check for cycles, run dfs and check to see if there are back edges. back edges
has v in (u,v) labeled "visiting", or "-1" here in status[].
"""













