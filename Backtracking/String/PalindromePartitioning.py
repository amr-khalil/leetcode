"""
Problem: Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example:
Input: "aab"
Output: [["a","a","b"],["aa","b"]]
"""

def palindrome_partitioning(s):
    res = []
    def backtrack(start, path):
        if start == len(s):
            res.append(path)
            return
        
        for i in range(start, len(s)):
            if is_palindrome(s, start, i):
                backtrack(i + 1, path + [s[start:i+1]])

    def is_palindrome(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    backtrack(0, [])
    return res


print(palindrome_partitioning("aab")) # [["a","a","b"],["aa","b"]]
