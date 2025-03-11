"""
Problem: Letter Combinations of a Phone Number
Given a string containing digits from 2-9,
return all possible letter combinations that the number could represent (like phone keypad letters).

A mapping of digit to letters (just like on the telephone buttons) is given below:
{
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""

digit_to_letters = {
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}

def letter_combinations(digits):
    res = []
    def backtrack(solution, start):
        if start == len(digits):
            res.append(''.join(solution))
            return
        
        choices = digit_to_letters[digits[start]]
        for i in range(len(choices)):
            solution.append(choices[i])
            backtrack(solution, start + 1)
            solution.pop()

    if not digits:
        return res
    
    backtrack([], 0)
    return res


digits = "23"
print(letter_combinations(digits)) # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]




# all possible combinations of the elements of the array
def all_combinations(arr):
    res = []
    def backtrack(solution, start):
        if start == len(arr):
            res.append(''.join(solution))
            return
        
        choices = arr[start]
        for i in range(len(choices)):
            solution.append(choices[i])
            backtrack(solution, start + 1)
            solution.pop()

    backtrack([], 0)
    return res


arr = ['123', '4567']
print(all_combinations(arr))




def all_cobmi(arr):
    res = []
    def backtrack(solution, start):
        if start == len(arr):
            res.append(solution[:])
            return
        
        choices = arr[start]
        for choice in choices:
            backtrack(solution + choice, start+1)

    backtrack("", 0)
    return res

arr = ['123', '4567', '9']
print(all_cobmi(arr))
