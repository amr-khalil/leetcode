"""
Problem: Subsets II (with duplicates)"
Given an integer array nums that may contain duplicates, return all possible subsets. The solution set must not contain duplicate subsets."
Example:
Input: nums = [1, 2, 2]
Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
"""

def subsets_with_duplicates(nums):
    nums.sort()
    res = []
    def backtrack(solution, choices):
        res.append(solution[:])

        for i in range(len(choices)):
            if i > 0 and choices[i] == choices[i-1]:
                continue
            solution.append(choices[i])
            backtrack(solution, choices[i+1:])
            solution.pop()

    backtrack([], nums)
    return res

nums = [1, 2, 2]
print(subsets_with_duplicates(nums)) # [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
