"""
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.
You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
While moving from building i to building i+1 (0-indexed),
If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

Example 1:
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

Example 2:
Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7

Example 3:
Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3
"""


from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # DP O(nbl) b for number of bricks, l for number of ladders
        # time limit exceeded
        
        
        """
        if len(heights) <= 1:
            return 0
        else:
            diff = heights[0] - heights[1]
            if diff >= 0:
                return self.furthestBuilding(heights[1:], bricks, ladders) + 1
            elif -diff <= bricks and ladders > 0:
                return max(self.furthestBuilding(heights[1:], bricks + diff, ladders), self.furthestBuilding(heights[1:], bricks, ladders - 1)) + 1
            elif ladders > 0:
                return self.furthestBuilding(heights[1:], bricks, ladders - 1) + 1
            elif -diff <= bricks:
                return self.furthestBuilding(heights[1:], bricks + diff, ladders) + 1
            else:
                return 0
                
        """
        
        # Min-heap
        # O(nlogn) time
        # heap insert and pop both take O(logn)
        # O(n) space
        
        hp, n = [], len(heights)
        
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                heapq.heappush(hp, diff)
                if len(hp) > ladders:
                    bricks -= heapq.heappop(hp)
                    if bricks < 0:
                        return i

        return n - 1
        
            
            