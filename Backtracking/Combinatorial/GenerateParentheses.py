"""
Problem: Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:
Input: n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
"""

def generate_parentheses(n):
    res = []
    def backtrack(open, close, path):
        if len(path) == 2 * n:
            res.append(path)
            return
        if open < n:
            backtrack(open + 1, close, path + '(')
        if close < open:
            backtrack(open, close + 1, path + ')')

    backtrack(0, 0, "")
    return res


print(generate_parentheses(3))
# ["((()))", "(()())", "(())()", "()(())", "()()()"]