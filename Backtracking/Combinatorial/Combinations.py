"""
Problem: Combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
Example:
Input: n = 4, k = 2
Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
"""

def combinations(n, k):
    res = []
    def backtrack(solution, choices):
        if len(solution) == k:
            res.append(solution[:])
            return
        
        for i in range(len(choices)):
            solution.append(choices[i])
            backtrack(solution, choices[i+1:])
            solution.pop()

    nums = list(range(1,n+1))
    backtrack([], nums)

    return res


print(combinations(4, 2)) # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]