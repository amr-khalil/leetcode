"""
Problem: Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.

Example:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6], [1,2,5], [1,7], [2,6]]
"""
def combinationSum2(candidates, target):
    res = []
    def backtrack(solution, choices, target):
        if target == 0:
            res.append(solution[:])
            return
        for i in range(len(choices)):
            # skip duplicates
            if i > 0 and choices[i] == choices[i-1]:
                continue
            # if the current choice is greater than the target, skip it
            if choices[i] > target:
                continue
            solution.append(choices[i])
            backtrack(solution, choices[i+1:], target - choices[i])
            solution.pop()

    # sort the candidates to avoid duplicates
    candidates.sort()
    backtrack([], candidates, target)
    return res

print(combinationSum2([10,1,2,7,6,1,5], 8)) # [[1,1,6], [1,2,5], [1,7], [2,6]]

