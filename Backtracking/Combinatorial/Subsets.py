"""
Problem: Subsets
Given a set of distinct integers, return all possible subsets.
Example:
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
"""

def subsets(nums):
    res = []
    def backtrack(solution, choices):
        res.append(solution[:])
        
        for i in range(len(choices)):
            solution.append(choices[i])
            backtrack(solution, choices[i+1:])
            solution.pop()

    backtrack([], nums)
    return res

nums = [1,2,3]
print(subsets(nums)) # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]


    

