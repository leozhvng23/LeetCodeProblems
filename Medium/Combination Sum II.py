"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # each number can only be used once
        [1, 1, 2, 5, 6, 7, 10]

        res = []
        n = len(candidates)
        candidates.sort()

        def dfs(idx, path, target):
            if target <= 0:
                if target == 0:
                    res.append(path)
                return

            # keep track of previous
            prev = -1

            for i in range(idx, n):
                num = candidates[i]
                if num == prev:
                    continue  # skip same number
                dfs(i + 1, path + [num], target - num)
                prev = num

        if n > 0:
            dfs(0, [], target)

        return res
