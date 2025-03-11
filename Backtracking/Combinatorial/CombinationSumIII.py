"""
Problem: Combination Sum III
Find all valid combinations of k numbers that sum up to n, using numbers from 1 to 9 only once.
The solution set must not contain duplicate combinations.

Example:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation: 1 + 2 + 4 = 7

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
Explanation: 1 + 2 + 6 = 9, 1 + 3 + 5 = 9, 2 + 3 + 4 = 9
"""

def combinationSum3(k, n):
    res = []
    def backtrack(solution, choices, target):
        if target == 0 and len(solution) == k:
            res.append(solution[:])
            return
        for i in range(len(choices)):
            if choices[i] > target:
                continue

            solution.append(choices[i])
            backtrack(solution, choices[i+1:], target - choices[i])
            solution.pop()

    nums = list(range(1,10))
    backtrack([], nums, n)
    return res


print(combinationSum3(3, 7)) # [[1,2,4]]
print(combinationSum3(3, 9)) # [[1,2,6], [1,3,5], [2,3,4]]