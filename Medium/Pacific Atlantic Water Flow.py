"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
"""
from typing import List

# O(M*N) time
# O(M*N) space

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific, atlantic = set(), set()
        M, N = len(heights), len(heights[0])
                        
        def dfs(r, c, ocean, prev):
            if (r not in range(M) or c not in range(N) or 
                (r, c) in ocean or heights[r][c] < prev):
                return
        
            ocean.add((r,c))

            for i, j in [[0,1],[0,-1],[1,0],[-1,0]]:
                dfs(r+i, c+j, ocean, heights[r][c])
                    
        for r in range(M):
            for c in range(N):
                if r == 0 or c == 0:
                    dfs(r, c, pacific, float('-inf'))
                if r == M-1 or c == N-1:
                    dfs(r, c, atlantic, float('-inf'))
                
        return list(pacific.intersection(atlantic))


"""
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # run bfs from both atlantic and pacific and find the intersection
        # 2 queues one for atlantic one for pacific
        # runtime: O(mn)
        # space: O(mn)

        if not heights or not heights[0]:
            return []

        pq, aq = deque(), deque()  # pacific queue, atlantic queue
        pv, av = set(), set()  # pacific visited[], atlantic visited[]
        rows, cols = len(heights), len(heights[0])

        # return qualifying neighboring nodes
        def neighbors(node):
            x, y = node[0], node[1]
            adj = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
            for i, j in adj:
                if 0 <= i < rows and 0 <= j < cols and heights[x][y] <= heights[i][j]:
                    yield i, j

        # initialize pacific and atlantic queues
        for r in range(rows):
            pq.append((r, 0))
            aq.append((r, cols - 1))
        for c in range(cols):
            pq.append((0, c))
            aq.append((rows - 1, c))

        def bfs(queue, visited):
            # initialize BFS Search -> add all shore nodes to queue
            while queue:
                curr = queue.popleft()
                visited.add(curr)
                # put all qualified neighbors on queue
                for n in neighbors(curr):
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)

        bfs(pq, pv)  # pacific BFS search
        bfs(aq, av)  # atlantic BFS search

        # find intersection and convert to list
        return list(pv.intersection(av))


        # DP implementation

        # DOES NOT WORK!!! because its one directional so it does not work for all directions!
        
        if len(heights) == 0 or len(heights[0]) == 0:
            return []
        
        rows = len(heights)
        cols = len(heights[0])
        
        # make DP matrix for atlantic and pacific
        # 0: unqualified, 1: qualified
        pacific = [[0]*(cols) for _ in range(rows)]
        atlantic = [[0] * (cols) for _ in range(rows)]
        
        # add all shore notes
        for c in range(cols):
            pacific[0][c] = 1
            atlantic[rows-1][c] = 1
        for r in range(rows):
            pacific[r][0] = 1
            atlantic[r][cols-1] = 1
            
        # Fill DP pacific 
        # [i][j] = 1 iff (left cell = 1 and left cell height >= curr cell height)
        # or (up cell = 1 and height >= curr cell height)
        # fill it from top left to bottom right
        
        for i in range(1, rows):
            for j in range(1, cols):
                if (pacific[i-1][j] == 1 and heights[i-1][j] <= heights[i][j]) or (pacific[i][j-1] == 1 and heights[i][j-1] <= heights[i][j]):
                    pacific[i][j] = 1
                    
        # fill DP atlantic
        # fill from bottom right to top left
        
        for i in range(rows-2, -1, -1):
            for j in range(cols-2, -1, -1):
                if (atlantic[i+1][j] == 1 and heights[i+1][j] <= heights[i][j]) or (atlantic[i][j+1] == 1 and heights[i][j+1] <= heights[i][j]):
                    atlantic[i][j] = 1
        
        # find common cells in both DP matrices
        
        ans = []
        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    ans.append([i,j])
                    
        print(pacific)
        
        return ans
"""