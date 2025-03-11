"""
Problem: Combination Sum
Given an array of distinct integers candidates and a target integer target,
return all unique combinations of candidates where the chosen numbers sum to target. The same number may be chosen multiple times.

Example:
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]
"""

def combination_sum(candidates, target):
    res = []
    def backtrack(solution, choices, target):
        if target == 0:
            res.append(solution[:])
            return
        
        for i in range(len(choices)):
            if choices[i] > target:
                continue
            solution.append(choices[i])
            backtrack(solution, choices[i:], target - choices[i])
            solution.pop()

    backtrack([],candidates, target)
    return res

candidates = [2, 3, 6, 7]
target = 7
print(combination_sum(candidates, target)) # [[2, 2, 3], [7]]

