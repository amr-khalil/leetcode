"""
Problem: Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Example:
Input: s = "()"
Output: True

Input: s = "()[]{}"
Output: True

Input: s = "(]"
Output: False
"""

def validParentheses(s):
    stack = []
    hashmap = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in hashmap:
            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            top_element = stack.pop() if stack else "#"

            # The mapping for the opening bracket in our hash and the top
            # element of the stack don't match, return False
            if top_element != hashmap[char]:
                return False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(char)

    return not stack

# Example usage
s = "()"
print(validParentheses(s)) # True

s = "()[]{}"
print(validParentheses(s)) # True

s = "(]"
print(validParentheses(s)) # False