"""
Problem: Combinations Test
Generate all possible combinations of a given array of strings.
Example:
Input: ['abc', 'def']

Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""

def combinations_test(arr):
    res = []
    def backtrack(solution, start):
        if start == len(arr):
            res.append(solution[:])
            return
        
        choices = arr[start]
        for choice in choices:
            solution += choice
            backtrack(solution, start + 1)
            solution = solution[:-1]

    
    backtrack("", 0)
    return res


arr = ['abc', 'def']
print(combinations_test(arr))
