"""
Problem: Permutations II (with duplicates)
Given a collection of numbers nums that may contain duplicates, return all unique permutations.
Example:
Input: nums = [1, 1, 2]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
"""

def permutations_with_duplicates(nums):
    nums.sort()
    res = []
    def backtrack(solution, choices):
        if len(solution) == len(nums):
            res.append(solution[:])
            return
        
        for i in range(len(choices)):
            # if the current choice is the same as the previous choice, then skip
            if i > 0 and choices[i] == choices[i-1]:
                continue
            solution.append(choices[i])
            backtrack(solution, choices[:i] + choices[i+1:])
            solution.pop()
    backtrack([], nums)
    return res

nums = [1, 1, 2] 
print(permutations_with_duplicates(nums)) # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

from collections import Counter
def permutations_with_duplicates_hashmap(nums):
    res = []
    counter = Counter(nums)
    def backtrack(solution):
        if len(solution) == len(nums):
            res.append(solution[:])
            return
        
        for choice in counter:
            if counter[choice] > 0:
                solution.append(choice) # make choice
                counter[choice] -= 1
                backtrack(solution) # backtrack
                counter[choice] += 1
                solution.pop() # undo choice
    backtrack([])

    return res

nums = [1, 1, 2]
print(permutations_with_duplicates_hashmap(nums)) # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
