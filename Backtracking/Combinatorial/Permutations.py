"""
Problem: Permutations
Given a collection of distinct integers, return all possible permutations.
Example:
Input: nums = [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""

def permutations(nums):
    def backtrack(solution, choices):
        # if compelete solution
        if len(solution) == len(nums):
            res.append(solution[:])
            return
        
        for i in range(len(choices)):
            solution.append(choices[i]) # make choice
            backtrack(solution + choices[i], choices[:i] + choices[i+1:]) # backtrack
            solution.pop() # undo choice
    
    res  = []
    backtrack([], nums)

    return res 

nums = [1, 2, 3]
print(permutations(nums))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
            